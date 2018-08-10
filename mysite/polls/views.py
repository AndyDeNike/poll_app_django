# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
#there is also the get_list_or_404() that uses 'filter()' instead of get
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse 
from django.views import generic 

from .models import Choice, Question

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last give published questions."""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else: 
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data.  This prevents data from being used twice if a 
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	#return HttpResponse("You're voting on question %s." % question_id)

		
'''
def index(request):
	#return HttpResponse("Hello, world.  You're at the polls index.")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in latest_question_list])
	#loads template and passes context 
	#template = loader.get_template('polls/index.html')
	#context creates a dictionary which connects template variables to 
	#views in python objects 
	context = {'latest_question_list': latest_question_list}
	#return HttpResponse(template.render(context, request))
	#^ rewritten: 
	#render takes the request object as 1st argument, template name as
	#2nd argument, and a dictionary with template variables as optional 
	#3rd argument
	#returns HttpResponse object of template rendered w/ given context
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id): 
	#try:
		#question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
		#raise Http404("Question does not exist")
	question = get_object_or_404(Question, pk=question_id)
	#this sends the params {'q':q} to detail.html to be used as a variable	
	return render(request, 'polls/detail.html', {'question': question})

	#return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})
	#response = "You're looking at the results of quesiton %s."
	#eturn HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else: 
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data.  This prevents data from being used twice if a 
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	#return HttpResponse("You're voting on question %s." % question_id)
'''
