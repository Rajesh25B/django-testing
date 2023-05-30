from django.urls import path
from .views import homePage, indexPage


urlpatterns = [
    path('', indexPage),
    path('home', homePage),
]
