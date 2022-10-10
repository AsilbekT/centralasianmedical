from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    news = New.objects.all()
    events = Event.objects.all()

    try:
        status = Status.objects.get(id=1)
    except:
        status = None

    context = {"news": news, "status": status, "events": events}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about-us.html")


def contact(request):
    return render(request, "contacts.html")

def news(request):
    news = New.objects.all()

    context = {"news": news}
    return render(request, "grid-news.html", context)


def news_details(request, slug):
    news = New.objects.get(slug=slug)

    context = {"news": news}
    return render(request, "news-post-page.html", context)




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


def event_details(request, slug):
    return render(request, "event-page.html")


def team(request):
    return render(request, "team.html")


def team_details(request, id):
    try:
        team_member = Workers.objects.get(id=id)
    except ObjectDoesNotExist:
        team_member = None

    context = {"team_member": team_member}
    return render(request, "team-member-profile.html", context)


def search_result(request):
    return render(request, "search-results.html")