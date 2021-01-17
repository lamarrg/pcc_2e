"""defines URL patterns for pizzas"""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    # Home page
	path('', views.index, name='index'),
	# page that shows all pizzas
	path('pizzas/', views.pizzas, name='pizzas'),
	# page that shows ingredients in each pizza
	path('pizzas/<int:pizza_id>/', views.pizza, name='pizza')
]
