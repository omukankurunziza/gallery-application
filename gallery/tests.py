from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.brouchette = Image(name = 'brouchette', description = 'it Rwandan food called brouchette')
        self.brouchette.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.brouchette, Image))


    def test_save_method(self):
        self.food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 


    def test_delete_method(self):
        self.new_image = Image(name = 'brouchette', description = 'it Rwandan food called brouchette')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)


    def test_update_method(self):
        self.vic = Image(name = 'gallery', description = 'an image of Gallery')
        self.vic.save_image()
        self.vic = Image(name = 'gallery', description = 'an image of Gallery')        
        self.vic.update_image(name = 'gallery')
        self.vic.save_image()
        images = Image.objects.filter(name = 'gallery')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.travel = Category(name = 'Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel, Category))

    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)        

    def test_delete_method(self):
        self.new_category = Category(name = 'Foood')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)   

    def test_update_category(self):
        self.health = Category(name = 'Foood')
        self.health.save_category()
        self.health = Category(name = 'Fashion')
        self.health.save_category()
        self.health.update_category(name = 'Travel')
        categories = Category.objects.filter(name = 'kigali')
        self.assertEqual(len(categories), 1)




class LocationTestClass(TestCase):    
    def setUp(self):
        self.China = Location(name = ' China')

    def test_instance(self):
        self.assertTrue(isinstance(self.China, Location))

    def test_save_method(self):
        self.China.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location = Location(name = 'china')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

    def test_update_method(self):
        self.Kigali = Location(name = 'Kigali')
        self.Kigali.save_location()
        self.Kigali = Location(name = 'Kigali')
        self.Kigali.save_location()
        selfKigali.update_location(name = 'Kigali')
        locations = Location.objects.filter(name = 'Kigali')
        self.assertEqual(len(locations), 1)   