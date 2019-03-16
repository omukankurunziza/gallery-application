from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
   
    def __str__(self):
        return self.name
        
    def save_location(self):
        self.save()    

    def delete_location(self):
        Location.objects.filter(id = self.pk).delete()
   
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)  
class Category(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()    

    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()
    
    def update_category(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length =70)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    
    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)       

    @classmethod
    def all_pictures(cls):
        pictures = cls.objects.all()
        return pictures 

    @classmethod
    def picture_locations(cls):
        pictures = cls.objects.order_by('location')
        return pictures 

    @classmethod
    def picture_categories(cls):
        pictures = cls.objects.order_by('category')
        return pictures 

    @classmethod
    def get_picture(cls, id):
        picture = cls.objects.get(id=id)
        return picture

    @classmethod
    def search_by_category(cls, search_input):
        images = cls.objects.filter(category__name__icontains=search_input)
        return images        

    class Meta:
        ordering = ['name']


