from django.shortcuts import render
from django.views import View


class CarView(View):
    template_name = 'cars/cars.html'
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
