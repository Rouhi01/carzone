from django.views import View
from django.shortcuts import render


class HomeView(View):
    template_name = 'pages/home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self):
        pass


class AboutView(View):
    template_name = 'pages/about.html'
    def get(self, request):
        return render(request, self.template_name)
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
        pass