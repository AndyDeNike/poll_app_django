from django.urls import path 

from . import views 

#path()argument contains 2 required parameters and 2 optional: 
#1st 'route': a string that contains a URL pattern that when requested,
#is searched for in the urlpatterns list
#2nd 'view': when mathc route match is found, Django calls specified 
#view function, ex. views.whatever 
#3rd 'kwargs': arbitrary keyword arguments can be passed to dictionary
#to target the view 
#4th 'name': name your url, allowing you to access/refer to it with 
#this title/label 


app_name = 'polls'
urlpatterns = [
	# ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

