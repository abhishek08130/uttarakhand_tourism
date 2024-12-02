from django.shortcuts import render
from main import models

# Create your views here.


def index(request):
    places = models.Place.objects.all()
    if request.method == 'POST':
        email = request.POST.get("email")
        print(email)
        obj = models.sub.objects.create(email=email)
        obj.save()
    return render(request, "index.html", {"places": places})


def places(request, name):
    place = models.Place.objects.get(slug=name)
    all_place = models.Place.objects.all()
    return render(request, "single-blog.html", {"place": place, "all_place": all_place})
