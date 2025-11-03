from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    work_ex = models.IntegerField()  
    dob = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



