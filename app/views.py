from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
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
    gallery = Gallery.objects.all().order_by('-id')[:10]

    context = {"news": news, "gallery": gallery}
    return render(request, "grid-news.html", context)


def news_details(request, slug):
    news = New.objects.get(slug=slug)
    gallery = Gallery.objects.all().order_by('-id')[:10]

    context = {"news": news, "gallery": gallery}
    return render(request, "news-post-page.html", context)


def courses(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "course-grid.html", context)


def course_details(request, slug):
    course = Course.objects.get(slug=slug)
    context = {"course": course}
    return render(request, "course-details.html", context)


def gallery(request):
    gallery = Gallery.objects.all()

    context = {"gallery": gallery}
    return render(request, "gallery.html", context)


def history(request):
    return render(request, "history.html")



def events(request):
    events = Event.objects.all()

    context = {"events": events}
    return render(request, "events.html", context)


def event_details(request, slug):
    event = Event.objects.get(slug=slug)
    other_events = Event.objects.filter(~Q(slug=slug))
    context = {"event": event, "other_events": other_events}

    return render(request, "event-page.html", context)


def team(request):
    members = Workers.objects.all()

    context = {"members": members}
    return render(request, "team.html", context)


def team_details(request, id):
    try:
        team_member = Workers.objects.get(id=id)
    except ObjectDoesNotExist:
        team_member = None

    context = {"team_member": team_member}
    return render(request, "team-member-profile.html", context)


def leader(request):
    members = Leaders.objects.all()

    context = {"members": members}
    return render(request, "team.html", context)


def leader_details(request, id):
    try:
        team_member = Leaders.objects.get(id=id)
    except ObjectDoesNotExist:
        team_member = None

    context = {"team_member": team_member}
    return render(request, "team-member-profile.html", context)

def search_result(request):
    return render(request, "search-results.html")