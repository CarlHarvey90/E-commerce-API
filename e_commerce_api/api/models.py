from django.db import models

class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='change@me.com')
    username = models.CharField(max_length=255, default='Test')
    password = models.CharField(max_length=255, default='123')

    def __str__(self):
        return self.firstname