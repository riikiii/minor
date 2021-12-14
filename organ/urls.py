from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read/', views.read, name='read'),
    path('family/', views.family, name='family'),
    path('stories', views.stories, name='stories'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('donor/story/<int:pk>', views.donor_story, name='donor')
]