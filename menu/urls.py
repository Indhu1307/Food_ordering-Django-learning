from django.urls import path
from  .import views # connecting views page here

urlpatterns = [
    path('', views.food_list, name='food_list'),
]