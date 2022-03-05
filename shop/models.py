from django.db import models
from django.contrib.auth.models import User
from matplotlib.style import use

# Create your models here.

class Category(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    name = models.CharField(db_column="name", max_length=255, null=True, blank=True)
    class Meta: 
        db_table = 'Category'

class PublishingCompany(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    name = models.CharField(db_column="name", max_length=255,null=True, blank=True)
    address = models.CharField(db_column="address", max_length=255, null= True, blank= True)
    phoneNumber = models.CharField(db_column="phoneNumber", max_length=11, null=True, blank= True)
    email = models.CharField(db_column="email", max_length=100, null=True, blank= True)
    class Meta:
        db_table = 'PublishingCompany'

class Book(models.Model):
    id = models.AutoField(db_column="ID",primary_key=True)
    categoryID = models.ForeignKey(Category,models.CASCADE, db_column="categoryID")
    publishingCompanyID = models.ForeignKey(PublishingCompany, models.DO_NOTHING,db_column="publishingCompanyID")
    name = models.CharField(db_column="name", max_length=255, null=True, blank=True)
    description = models.CharField(db_column = "description", max_length=2550, null= True, blank=True)
    numberOfPages = models.IntegerField(db_column="numberOfPages", null=True, blank=True, default=1)
    author = models.CharField(db_column="author", max_length=255, null=True, blank=True)
    price = models.IntegerField(db_column="price", null=True, blank=True, default=10000)
    image = models.CharField(db_column="image", max_length=255, null=True, blank=True)
    class Meta: 
        db_table = 'Book'

class BookItem(models.Model):
    id = id = models.AutoField(db_column="ID",primary_key=True)
    bookID = models.ForeignKey(Book,models.CASCADE, db_column="bookID",)
    discount = models.FloatField(db_column="discount", blank=True, null= True, max_length=255, default=0)
    startDay = models.DateTimeField(db_column="startDay",blank=True, max_length=255, null=True,auto_now_add=True)
    endDay = models.DateTimeField(db_column="endDay", blank=True, max_length=255, null=True,auto_now_add=True)
    image =  models.CharField(db_column="image", max_length=255, null=True, blank=True)
    class Meta: 
        db_table = 'BookItem'
