from django.urls import path
from . import views

#urlconfig for the resource_main
urlpatterns = [
    path('', views.index, name="index"),
]
