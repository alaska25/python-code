from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GroceryItem(models.Model):
	item_name = models.CharField(max_length=50)
	category = models.CharField(max_length=200)
	status = models.CharField(max_length=50, default="pending")
	date_created = models.DateTimeField('date created')
	user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

