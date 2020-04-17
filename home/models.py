from django.db import models
# from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser

# Create your models here.
LANGUAGE_CHOICES = (
		('en-us', 'English'),
		('nl', 'Dutch'),
		('hi', 'Hindi'),
	)
class User(AbstractUser):
	is_trailing = models.BooleanField(default=True)
	language = models.CharField(default='en-us', choices=LANGUAGE_CHOICES, max_length=5)

class LangTranslation(models.Model):
	language = models.CharField(default='en-us', choices=LANGUAGE_CHOICES, max_length=5)
