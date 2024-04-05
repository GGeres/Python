from django.urls import path
from galeria.views import index

yrlpatterns = [
    path('', index)
]