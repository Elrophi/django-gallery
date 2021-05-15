from django.shortcuts import render
from .models import Image, Location

# Create your views here.
def home(request):
    # images = Image.objects.all()
    # locations = Location.get_location()
    return render(request, 'pictures/home.html')
