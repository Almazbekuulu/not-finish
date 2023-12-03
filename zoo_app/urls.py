from django.urls import path
from .views import list_pets, book_pet, buy_pet

urlpatterns = [
    path('', list_pets, name='list_pets'),
    path('book_pet/<int:pet_id>/', book_pet, name='book_pet'),
    path('buy_pet/<int:pet_id>/', buy_pet, name='buy_pet'),
]