from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views import View
from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib import messages


class HomeView(View):
    template_name = 'pages/home.html'

    def setup(self, request, *args, **kwargs):
        self.teams_instance = Team.objects.all()
        self.cars_instance = Car.objects.all()
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        featured_cars = self.cars_instance.filter(is_featured=True).order_by('-created_at')
        latest_cars = self.cars_instance.order_by('-created_at')
        # search_fields = self.cars_instance.values('model', 'year', 'city', 'body_style')
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
        context = {
            'teams':self.teams_instance,
            'featured_cars': featured_cars,
            'latest_cars': latest_cars,
            # 'search_fields':search_fields,
            'model_search':model_search,
            'city_search':city_search,
            'year_search':year_search,
            'body_style_search':body_style_search,
        }
        return render(request, self.template_name, context)

    def post(self):
        pass


class AboutView(View):
    template_name = 'pages/about.html'

    def setup(self, request, *args, **kwargs):
        self.teams_instance = Team.objects.all()
        super().setup(request, *args, **kwargs)
    def get(self, request):
        context = {
            'teams':self.teams_instance,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        pass


class ServicesView(View):
    template_name = 'pages/services.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pass


class ContactView(View):
    template_name = 'pages/contact.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        message_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\Message: {message}'

        # send email
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = f'You have a new message from Carzone website regarding {subject}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [admin_email,]
        send_mail(email_subject, message_body, email_from, recipient_list, fail_silently=False)

        messages.success(request, 'Thank you for contacting us, We will get back to you shortly.')
        return redirect('pages:contact')