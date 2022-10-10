from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('news/', views.news, name="news"),
    path('news/<slug:slug>/', views.news_details, name="news_details"),
    path('courses/', views.courses, name="courses"),
    path('gallery/', views.gallery, name="gallery"),
    path('history/', views.history, name="history"),
    path('course_details/', views.course_details, name="course_details"),
    path('events/', views.events, name="events"),
    path('events/<slug:slug>/', views.event_details, name="event_details"),
    path('team/', views.team, name="team"),
    path('team/<int:id>/', views.team_details, name="team_details"),
    path('search_result/', views.search_result, name="search_result"),
]
