# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime 

from django.db import models
from django.utils import timezone




# Create your models here.
# Each model has a number of class variables that represent a database
# field in the model.

# Each field is represented by an instance of a Field class (eg CharField,
# DateTimeField, etc) that determines the type of data the field holds.



class Question(models.Model):
	# The name of each Field instance (eg question_text/pub_date) is the
	# fields name in machine-readable code (used for Python code/database 
	# column name)

	# some Field classes have required arguments, such as CharField
	# with max_length

	question_text = models.CharField(max_length=200)
	# Optional first argument can represent human readable name for Field
	# if arugment not given, Field instance name is default 
	pub_date = models.DateTimeField('date published')

	#human readable: 
	def __str__(self):
		return self.question_text 

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		was_published_recently.admin_order_field = 'pub_date'
		was_published_recently.boolean = True
		was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	# optional argument default is set to 0 for votes 
	votes = models.IntegerField(default=0)

	#creates human readable string of text
	def __str__(self):
		return self.choice_text

