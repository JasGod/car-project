from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, Paginator
from django.core.exceptions import BadRequest

# Create your views here.
"""
Defines the views for the 'cars' application.

This module contains view functions that handle the display of car listings,
car details, and search functionality for cars.
"""

def cars(request):
    """
    Displays a paginated list of all available cars.

    Retrieves all Car objects, ordered by creation date (newest first),
    and paginates them. Also provides distinct values for model, city, year,
    and body style to populate search/filter dropdowns in the template.

    Renders:
        cars/cars.html

    Context Variables:
        cars: Page object containing the cars for the current page.
        model_search: Distinct car models.
        city_search: Distinct car cities.
        year_search: Distinct car years.
        body_style_search: Distinct car body styles.
    """
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4) # Show 4 cars per page
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    """
    Displays the detailed information for a single car.

    Retrieves a Car object by its ID or returns a 404 error if not found.

    Renders:
        cars/car_detail.html

    Context Variables:
        single_car: The Car object to be displayed.
    """
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request,'cars/car_detail.html', data)


def search(request):
    """
    Handles the car search functionality based on user-submitted criteria.

    Filters cars based on various GET parameters such as keyword, model, city,
    year, body style, and price range. Also provides distinct values for
    various car attributes to populate search filter dropdowns in the template.

    Renders:
        cars/search.html

    Context Variables:
        cars: QuerySet of cars matching the search criteria.
        model_search: Distinct car models.
        city_search: Distinct car cities.
        year_search: Distinct car years.
        body_style_search: Distinct car body styles.
        transmission_search: Distinct car transmission types.
    """
    cars = Car.objects.order_by('-created_date')

    # Fields for populating search filter dropdowns
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

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)


    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)


    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price: # Ensure max_price is not empty before filtering
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)
