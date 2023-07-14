from django.urls import path
from discussions import views

urlpatterns = [
   path('comment/create/', views.create_comment, name='create_comment'),
]