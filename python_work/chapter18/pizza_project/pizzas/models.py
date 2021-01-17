from django.db import models

# Create your models here.
class Pizza(models.Model):
	"""A pizza that is offered at the pizzeria"""
	name = models.CharField(max_length=200)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.name

class Topping(models.Model):
	"""A topping that goes on the pizza"""
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	class Meta: verbose_name_plural = 'toppings'

	def __str__(self):
		"""Return a string representation of the model"""
		return self.name
