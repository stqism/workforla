from django.db import models


class Category(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=128, unique=True)


class JobClass(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class_code = models.IntegerField(unique=True)
    classspec_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    occupational_category = models.CharField(max_length=200)
    skills = models.TextField()
    related_keywords = models.TextField()
    categories = models.ManyToManyField(Category)
    salary_low = models.IntegerField(default=0, null=False)
    salary_high = models.IntegerField(default=0, null=False)

    # URL fields
    external_url = models.URLField()
    career_ladder_url = models.URLField()

    # Large content fields
    description = models.TextField()
    qualifications = models.TextField()
    responsibilities = models.TextField()
    exam_notes = models.TextField()
