from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="21home"),
    path('practical_21', index),
]