from distutils.command.upload import upload
from hashlib import md5
from django.db import models

# Create your models here.

class Accounts(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.TextField()
    birth=models.DateField()
    def __str__(self):
        return self.fullname

class VendorAcc(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.TextField()
    def __str__(self):
        return self.fullname

# 
class Pro(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()
    price=models.CharField(max_length=10)
    ratting=models.CharField(max_length=10)
    image=models.ImageField(upload_to='media')
    v_id=models.CharField(max_length=10, default='')
    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(default='')
    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
