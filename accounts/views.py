from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from contacts.models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin




class RegisterView(View):
    template_name = 'accounts/register.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!', 'danger')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'Email already exists!', 'danger')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(
                        first_name=firstname,
                        last_name=lastname,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.success(request, 'You are registered successfully', 'success')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match', 'danger')
            return redirect('accounts:register')


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in successfully.')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('accounts:login')


class LogoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('pages:home')


class DashboardView(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    login_url = '/accounts/login/'

    def setup(self, request, *args, **kwargs):
        self.user_inquiries = Contact.objects.order_by('-created_at').filter(user_id=request.user.id)
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user_inquiries = self.user_inquiries
        context = {
            'user_inquiries':user_inquiries
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass