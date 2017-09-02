from django.db import models


class CategoryManager(models.Manager):
    def get_by_natural_key(self, category_name):
        return self.get(name=category_name)


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    objects = CategoryManager()

    slug = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=128, unique=True)

    def natural_key(self):
        return (self.name,)

    def __str__(self):
        return '<Category: [{slug}] {name}>'.format(
            slug=self.slug,
            name=self.name)


class JobClass(models.Model):

    class Meta:
        verbose_name_plural = "Job Classes"

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    # Human-friendly ID
    alias = models.CharField(default='', max_length=200, unique=True)

    # External identifiers
    class_code = models.IntegerField(unique=True)
    classspec_id = models.IntegerField(unique=True)

    title = models.CharField(max_length=200)
    occupational_category = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    related_keywords = models.CharField(max_length=200)
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

    def __str__(self):
        return '<JobClass: {title}'.format(title=self.title)
