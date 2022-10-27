from unittest.util import _MAX_LENGTH
from django.db import models
from pyexpat import model
# Create your models here.

from email.policy import default


# Create your models here.


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=[('admin','admin'),('user','user')], default='user')
    created_at = models.DateTimeField(
        ("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        ("تاریخ بروزرسانی"), auto_now=False, auto_now_add=True)



    
class Deploy(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    person_name = models.CharField(max_length=100)
    deploy_datetime = models.DateTimeField(
        ("تاریخ دیپلوی"), auto_now=False, auto_now_add=True)
    created_at = models.DateTimeField(
        ("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        ("تاریخ بروزرسانی"), auto_now=False, auto_now_add=True)


class person_deploy_mapper(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    deploy = models.ForeignKey(Deploy, on_delete=models.CASCADE)

   