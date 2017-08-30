from django.contrib import admin

from .models import Category
from .models import JobClass

admin.site.register(Category)
admin.site.register(JobClass)
