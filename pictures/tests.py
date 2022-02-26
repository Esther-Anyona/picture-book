from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Kenya')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    # Testing save method
    def test_save(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Testing delete method
    def test_delete(self):
        self.location.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='nature')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    # Testing save method
    def test_save(self):
        self.category.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    # Testing delete method
    def test_delete(self):
        self.category.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)

class ImageTestClass(TestCase):

    # set up method
    def setUp(self):
        self.location = Location(name='Kenya')
        self.location.save_location()

        self.category = Category(name='nature')
        self.category.save_category()
        
        self.image= Image(image='hallow', name='ugly', photographer='Anyona', description='not what I expected', location=self.location, category=self.category)
        self.image.save_image()
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing save method
    def test_save(self):
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    # Testing delete method
    def test_delete(self):
        self.image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)==0)