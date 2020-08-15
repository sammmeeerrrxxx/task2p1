from django.db import models
from django.db.models import Model

# Create your models here.
class user(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	phoneno=models.CharField(max_length=100)
	email = models.CharField(null=True, max_length=255)
	gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female'), ('o', 'Other')), blank=True,
                              )
	def __str__(self):
		return self.firstname
