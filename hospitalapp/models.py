from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=500)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    password = models.CharField(max_length=100)
    date = models.DateField(null=True)

    def __str__(self):
        return self.fullname

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)