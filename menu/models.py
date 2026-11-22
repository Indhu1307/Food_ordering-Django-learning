from django.db import models  #database table create 

# Create your models here.
class Category(models.Model): # creating  class

    category_name=models.CharField(max_length=100) # storing  value

    def __str__(self):  # spl fn - when obj is display what value should show
        return self.category_name

class Food(models.Model):  # creating new model class
    category = models.ForeignKey( # connecting food table to category
        Category,
        on_delete=models.CASCADE, #if category is deleted food items also delete
        related_name='foods'  # using category accessin g food items easy
    )

    food_name=models.CharField(max_length=100)  # storing food name
    description=models.TextField() # details about food
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(blank=True, null=True) # null - databse valure null
    is_available=models.BooleanField(default=True)

    def __str__(self):  #when obj is displayed what value shoiuld show
        return self.food_name