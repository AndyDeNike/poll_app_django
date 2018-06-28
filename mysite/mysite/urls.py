"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path 


#path()argument contains 2 required parameters and 2 optional: 
#1st 'route': a string that contains a URL pattern that when requested,
#is searched for in the urlpatterns list
#2nd 'view': when mathc route match is found, Django calls specified 
#view function, ex. views.whatever 
#3rd 'kwargs': arbitrary keyword arguments can be passed to dictionary
#to target the view 
#4th 'name': name your url, allowing you to access/refer to it with 
#this title/label  
urlpatterns = [
	

	path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #not sure what this is for: url(r'^admin/', admin.site.urls),
]
