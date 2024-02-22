from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('home_one/', views.home , name='home_one')
]