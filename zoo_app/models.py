
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Pet(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pet_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

class BookedPet(models.Model):
    phone_number = models.CharField(max_length=20)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='booked_pets')

class BoughtPet(models.Model):
    phone_number = models.CharField(max_length=20)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='bought_pets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
