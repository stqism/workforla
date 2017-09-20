# -*- coding: utf-8 -*-
import datetime
import logging
import sys

from bs4 import BeautifulSoup
import requests

from jobs.models import ExamDate


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
logger.addHandler(stream)


DOWNLOAD_URL = 'http://per.lacity.org/cfm/examinfo/download.cfm?page=1&sort=&dir=ASC&size=300&filterby=6&filter=&mode=xls'
CELLS_PER_ROW = 14


def parse_date(mmddyy_string):
    if not mmddyy_string:
        return None
    dt = datetime.datetime.strptime(mmddyy_string, '%m/%d/%y')
    return dt.date()


def download_exam_data():
    return requests.get(DOWNLOAD_URL).content.decode('utf-8')


def is_open_type(open_promo_field):
    if not open_promo_field:
        return False
    return 'open' in open_promo_field.lower()


def parse_html_blob(blob):
    soup = BeautifulSoup(blob, 'html.parser')

    # Discard the first three rows, which just contain table header elements
    all_rows = soup('tr')[3:]

    exam_data = {}
    for tr in all_rows:
        cells = tr('td')
        assert len(cells) == CELLS_PER_ROW
        if is_open_type(cells[2].string):
            continue

        class_code = int(cells[0].string)
        exam_data[class_code] = {
            'class_code': class_code,
            'open_date': parse_date(cells[4].string),
            'exam_date': parse_date(cells[6].string)
        }

    return exam_data


def has_new_exam_date(previous_exam_date, exam_data):
    return (exam_data['open_date'] != previous_exam_date.open_date or
            exam_data['exam_date'] != previous_exam_date.exam_date)


def report_changes(new_exams, updated_exams):

    def _fmt_exam(exam):
        return '{cc}\t{od}\t{ed}'.format(cc=exam.class_code,
                                         od=exam.open_date,
                                         ed=exam.exam_date)

    logger.info('New Exams')
    for exam in new_exams:
        logger.info(_fmt_exam(exam))

    logger.info('')
    logger.info('Updated Exams')
    for exam in updated_exams:
        logger.info(_fmt_exam(exam))


def update_exams():
    cc_to_exam = parse_html_blob(download_exam_data())
    previous_exams = {d.class_code: d for d in ExamDate.objects.all()}

    new_exams = []
    updated_exams = []
    for cc, new_exam_info in cc_to_exam.items():
        if cc in previous_exams:
            previous_exam = previous_exams[cc]
            if has_new_exam_date(previous_exam, new_exam_info):
                previous_exam.open_date = new_exam_info['open_date']
                previous_exam.exam_date = new_exam_info['exam_date']
                previous_exam.save()
                updated_exams.append(previous_exam)
        else:
            # Consider doing this in a bulk_create()
            new_exam = ExamDate(class_code=cc,
                                open_date=new_exam_info['open_date'],
                                exam_date=new_exam_info['exam_date'])
            new_exam.save()
            new_exams.append(new_exam)

    report_changes(new_exams, updated_exams)


def run():
    update_exams()
