from django.shortcuts import render
from .models import Food

# Create your views here.

def food_list(request):
    foods=Food.objects.filter()
    foods = Food.objects.filter(is_available=True) # available foods only
    return render(request,'menu/food_list.html',{'foods':foods})