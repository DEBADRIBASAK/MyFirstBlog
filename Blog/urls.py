from django.urls import path
from . import views

urlpatterns=[
	path('home/',views.home,name='home'),
	path('post/',views.post,name='post'),
	path('explore/',views.explore,name='explore'),
	path('read/(?P<key>[0-9A-Za-z]+)/',views.goto,name='read'),
	path('about/',views.about,name='about'),
]