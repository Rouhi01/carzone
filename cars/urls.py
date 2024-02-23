from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.CarsView.as_view(), name='cars'),
    path('<int:id>/', views.CarDetailView.as_view(), name='car_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]