from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()



