from django.db import models
import datetime as dt
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def __str__(self):
        return self.location_name

    @classmethod
    def get_location(cls):
        locations = Location.objects.all()
        return locations

    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


class Category(models.Model):
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

    def save_category(self):
        return self.save()

    def delete_category(self):
        return self.delete()


class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    author = models.CharField(max_length=60, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        return self.save()

    def delet_image(self):
        return self.delete()

    @classmethod
    def update_image(cls, id, value):
         cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_bby_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location


