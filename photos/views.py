from django.shortcuts import render
from .models import Image, Location

# Create your views here.
def home(request):
    # image = request.GET.get('image')
    # print('image:', image)
    images = Image.objects.all()
    locations = Location.get_location()
    return render(request, 'pictures/home.html', {'images': images[::-1], 'locations': locations})

def image_location(request, location):
    images =Image.filter_by_location(location)
    return render(request, 'pictures/location.html', {'location_images': images})

def search(request):
    if 'imagesearch' in request.GET and request.GET['imagesearch']:
        category = request.GET.get('imagesearch')
        searched_images = Image.search_image_by_category(category)
        print(searched_images)
        message = f'{category}'
        return render(request, 'pictures/search.html', {'message': message, 'images':searched_images})
    else:
        message = 'No images searched'
        return render(request, 'pictures/search.html', {'message':message})
