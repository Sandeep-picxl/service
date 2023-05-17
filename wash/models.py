from django.db import models


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
