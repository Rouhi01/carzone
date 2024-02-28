from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('inquiry/', views.InquireyView.as_view(), name='inquiry')
]