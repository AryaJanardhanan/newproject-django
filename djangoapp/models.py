from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    doc = models.FileField(upload_to='documents/', default=0)
    img = models.ImageField(upload_to='gallery/', default=0)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    des = models.CharField(max_length=100)

class Book(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bk_name = models.CharField(max_length=100)