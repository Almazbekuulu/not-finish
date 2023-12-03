from django.contrib import admin
from .models import Category, Pet, BookedPet, BoughtPet

admin.site.register(Category)
admin.site.register(Pet)
admin.site.register(BookedPet)
admin.site.register(BoughtPet)