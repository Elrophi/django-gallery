from django.test import TestCase

from .models import Image, Category, Location
# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.loc= Location(location_name = 'Nairobi')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc1,Location))

    def test_save_method(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = Location.update_location_id(self.loc.id)
        location.update_location('Donholm')
        location = Location.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Donholm')


class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat1 = Category(category_name = 'Sport')




class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.image1= Location(location_name = 'Nairobi')
        self.image1.save_location()
        
        self.new_image= Image(image_name = 'Amboseli', image_description = 'This is a random post',image_location = self.image1)
        self.new_image.save()