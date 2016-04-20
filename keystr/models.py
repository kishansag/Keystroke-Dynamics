from __future__ import unicode_literals

from django.db import models

# Create your models here.
class stroke(models.Model):
	timecsv = models.TextField()
	keycsv = models.TextField()
	spincsv = models.TextField()
	email = models.EmailField()

class matrix(models.Model):
	timecsv = models.TextField()
	keycsv = models.TextField()
	spincsv = models.TextField()
	email = models.EmailField()	