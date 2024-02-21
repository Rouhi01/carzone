from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.CarView.as_view(), name='cars')
]