from django.views import View
from django.shortcuts import render
from .models import Team

class HomeView(View):
    template_name = 'pages/home.html'

    def setup(self, request, *args, **kwargs):
        self.teams_instance = Team.objects.all()
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'teams':self.teams_instance
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
            'teams':self.teams_instance
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
        pass