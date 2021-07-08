from django.db import models
from django.db.models.base import Model

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Employee(models.Model):
    Name = models.CharField(max_length=20)
    PhoneNo = models.IntegerField()
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
