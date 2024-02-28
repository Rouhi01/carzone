from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

class InquireyView(View):
    def post(self, request):
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(car_id=car_id).exists()
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car.'
                                        'Please wait until we get back to you.')
                return redirect('cars:car_detail', car_id)
        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message
        )

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
        subject = 'New Car Inguiry'
        message = f'Hi, You have a new inquiry for the car {car_title}. Please login to your admin panel for more info.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rouhi0011@gmail.com',]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.', 'success')
        return redirect('cars:car_detail', car_id)
