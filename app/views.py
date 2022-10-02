from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about-us.html")


def contact(request):
    return render(request, "contacts.html")

def news(request):
    return render(request, "grid-news.html")

def courses(request):
    return render(request, "course-grid.html")

def course_details(request):
    return render(request, "course_details.html")

def gallery(request):
    return render(request, "gallery.html")

def history(request):
    return render(request, "history.html")

def course_details(request):
    return render(request, "course-details.html")


def events(request):
    return render(request, "events.html")


def event_details(request):
    return render(request, "event-page.html")


def team(request):
    return render(request, "team.html")


def team_details(request):
    return render(request, "team-member-profile.html")


def search_result(request):
    return render(request, "search-results.html")