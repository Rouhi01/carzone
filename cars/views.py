from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Car


class CarsView(View):
    template_name = 'cars/cars.html'
    def setup(self, request, *args, **kwargs):
        self.cars_instance = Car.objects.order_by('-created_at')
        super().setup(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        # Pagination
        paginator = Paginator(self.cars_instance, 4)
        page = request.GET.get('page')
        paged_cars = paginator.get_page(page)

        # Search Fields
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

        context = {
            'cars':paged_cars,
            'model_search': model_search,
            'city_search': city_search,
            'year_search': year_search,
            'body_style_search': body_style_search,
        }
        return render(request, self.template_name, context)


class CarDetailView(View):
    template_name = 'cars/car_detail.html'
    
    def setup(self, request, *args, **kwargs):
        self.car_instance = get_object_or_404(Car, id=kwargs['id'])
        super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'car':self.car_instance,
        }
        return render(request, self.template_name, context)


class SearchView(View):
    template_name = 'cars/search.html'
    def setup(self, request, *args, **kwargs):
        self.cars_instance = Car.objects.order_by('-created_at')
        super().setup(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        cars = self.cars_instance
        # Search Fields
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
        transmission_search = Car.objects.values_list('transmission', flat=True).distinct()


        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                cars = cars.filter(description__icontains=keyword)

        if 'model' in request.GET:
            model = request.GET['model']
            if model:
                cars = cars.filter(model__iexact=model)
        if 'body_style' in request.GET:
            body_style = request.GET['body_style']
            if body_style:
                cars = cars.filter(body_style__iexact=body_style)
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                cars = cars.filter(city__iexact=city)
        if 'year' in request.GET:
            year = request.GET['year']
            if year:
                cars = cars.filter(year__iexact=year)
        if 'transmission' in request.GET:
            transmission = request.GET['transmission']
            if transmission:
                cars = cars.filter(transmission__iexact=transmission)
        if 'min_price' in request.GET:
            min_price = request.GET['min_price']
            max_price = request.GET['max_price']
            if max_price:
                cars = cars.filter(price__gte=min_price, price__lte=max_price)
        context = {
            'cars':cars,
            'model_search': model_search,
            'city_search': city_search,
            'year_search': year_search,
            'body_style_search': body_style_search,
            'transmission_search':transmission_search
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass