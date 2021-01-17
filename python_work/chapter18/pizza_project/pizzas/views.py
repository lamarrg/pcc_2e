from django.shortcuts import render

from.models import Pizza, Topping

# Create your views here.
def index(request):
	"""The home page for Pizzas"""
	return render(request, 'pizzas/index.html')

def pizzas(request):
	"""Show all pizzas"""
	pizzas =  Pizza.objects.order_by('name')
	context = {'pizzas': pizzas}
	return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
	"""show a single pizza and its toppings"""
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.topping_set.order_by('name')
	context = {'pizza': pizza, 'toppings': toppings}
	return render(request, 'pizzas/pizza.html', context)
