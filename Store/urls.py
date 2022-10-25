from django import views
from django.urls import path 
from Store.views import page

urlpatterns = [
    path('home',page.as_view()),
]
