# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question

from django.contrib import admin 

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				 {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	#fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)