# workfor.la

A website for helping people find and apply for work in the City of Los Angeles.
Built by the folks at [Hack For LA](http://www.hackforla.org/).

## Overview

This is a [Django](https://www.djangoproject.com/) project deployed on [Heroku](https://www.heroku.com/).

## Setup

The development environment is a work in progress, but here are the current steps.

Clone:

```
git clone git@github.com:alexchao/workforla.git
```

Setup Python virtualenv (install Python 3.x if you haven't already):

```
cd workforla/
python -m venv env
```

Install dependencies:

```
env/bin/pip install -r requirements.txt
```

Spin up database (requires [Docker](https://www.docker.com/), but you could also just use a local install of MySQL):

```
docker-compose up
env/bin/python manage.py migrate
```

Preload some data:

```
env/bin/python manage.py loaddata categories.json
env/bin/python manage.py loaddata jobs.json
```

Start server:

```
heroku local web
```

## Tests

Run tests the standard Django way:

```
env/bin/python manage.py test
```

If you get a `ValueError: Missing staticfiles manifest entry for [some asset]`
error, run the following command then try again:

```
env/bin/python manage.py collectstatic
```
