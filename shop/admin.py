from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(PublishingCompany)
admin.site.register(Category)