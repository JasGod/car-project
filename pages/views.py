from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import  send_mail
from django.contrib import messages


# Create your views here.
"""
Defines the views for the 'pages' application.

This module contains view functions for rendering static and informational
pages such as the homepage, about us page, services page, and contact page.
It also handles the submission of the contact form.
"""

def home(request):
    """
    Renders the homepage.

    Fetches all team members, featured cars, all cars, and distinct values
    for car search filters (model, city, year, body style) to display on
    the homepage.

    Renders:
        pages/home.html

    Context Variables:
        teams: QuerySet of all Team objects.
        featured_cars: QuerySet of featured Car objects, ordered by creation date.
        all_cars: QuerySet of all Car objects, ordered by creation date.
        model_search: Distinct car models.
        city_search: Distinct car cities.
        year_search: Distinct car years.
        body_style_search: Distinct car body styles.
    """
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
    'teams':teams,
    'featured_cars': featured_cars,
    'all_cars':all_cars,
    'model_search': model_search,
    'city_search': city_search,
    'year_search': year_search,
    'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    """
    Renders the 'About Us' page.

    Fetches all team members to display on the page.

    Renders:
        pages/about.html

    Context Variables:
        teams: QuerySet of all Team objects.
    """
    teams =Team.objects.all()
    data = {
    'teams':teams,
    }
    return render(request, 'pages/about.html',data)

def services(request):
    """
    Renders the 'Services' page.

    This is a static page and does not pass any specific context data
    from models.

    Renders:
        pages/services.html
    """
    return render(request, 'pages/services.html')

def contact(request):
    """
    Renders the 'Contact Us' page and handles contact form submissions.

    If the request method is POST, it processes the contact form data,
    sends an email to the admin, displays a success message, and redirects
    back to the contact page.

    If the request method is GET, it renders the contact form.

    Renders:
        pages/contact.html
    """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'brendaank2001@gmail.com', # Sender's email address
                [admin_email], # List of recipient email addresses
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        return redirect('contact') # Redirect to avoid form resubmission on refresh

    # For GET request or if POST fails before redirect (though unlikely here)
    return render(request, 'pages/contact.html')
