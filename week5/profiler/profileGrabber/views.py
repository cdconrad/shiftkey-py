from django.shortcuts import render, get_object_or_404
from .models import SavedUser

def index(request):
    context = {}
    return render(request, 'profileGrabber/index.html', context)

def discover(request):
    profile = "cd_conrad"
    influencer = "NO"
    context = {
        'profile': profile,
        'influencer': influencer,
    }

    return render(request, 'profileGrabber/discover.html', context)


def collection(request):
    saved_users = SavedUser.objects.all()

    context = {
        'saved_users': saved_users,
    }

    return render(request, 'profileGrabber/collection.html', context)
