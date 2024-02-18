from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home')
]