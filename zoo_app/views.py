from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Pet, BookedPet, BoughtPet

def list_pets(request):
    pets = Pet.objects.all()
    return render(request, 'list_pets.html', {'pets': pets})

@require_POST
def book_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    phone_number = request.POST.get('phone_number')


    if BookedPet.objects.filter(pet=pet, phone_number=phone_number).exists():
        return JsonResponse({'status': 'error', 'message': 'Животное уже забронировано'})


    if pet.available:
        BookedPet.objects.create(pet=pet, phone_number=phone_number)
        return JsonResponse({'status': 'success', 'message': 'Бронирование успешно завершено'})

    return JsonResponse({'status': 'error', 'message': 'Некорректная опция'})


def buy_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    phone_number = request.POST.get('phone_number')


    if BookedPet.objects.filter(pet=pet, phone_number=phone_number).exists():
        return JsonResponse({'status': 'error', 'message': 'Животное забронировано и нельзя купить'})



    if pet.available:
        BoughtPet.objects.create(pet=pet, phone_number=phone_number, price=pet.price)
        pet.available = False
        pet.save()





        return JsonResponse({'status': 'success', 'message': 'Покупка успешно завершена'})



    return JsonResponse({'status': 'error', 'message': 'Некорректная опция'})