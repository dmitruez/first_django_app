from django.db import models

# Create your models here.

class Car(models.Model):
	name = models.CharField("Название автомобиля", max_length=30)
	