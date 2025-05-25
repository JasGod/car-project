from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import  send_mail
from django.contrib.auth.models import User

"""
Defines the views for the 'contacts' application.

This module contains view functions responsible for handling user inquiries
about cars. It processes form submissions, saves inquiry data, and notifies
administrators.
"""

def inquiry(request):
    """
    Handles the submission of a car inquiry form.

    This view only processes POST requests. It retrieves inquiry details from
    the form data, including car information and user contact details.
    If the user is authenticated, it checks if they have already made an
    inquiry for the same car to prevent duplicates.

    A new `Contact` object is created with the submitted data. The `user_id`
    is set to the authenticated user's ID or to 0 if the user is anonymous
    (note: storing 0 for anonymous users might need re-evaluation for clarity,
    `None` or a dedicated anonymous user ID might be better if referential
    integrity is a concern or if queries differentiate these).

    An email notification is sent to the superuser (admin) about the new inquiry.
    Finally, a success message is displayed to the user, and they are redirected
    to the detail page of the car they inquired about.

    If the request method is not POST, this view does not explicitly handle it,
    meaning direct navigation to this URL via GET would likely result in an
    error or an empty response unless mapped restrictively in `urls.py`.

    Form Data (POST):
        car_id, car_title, first_name, last_name, customer_need, city,
        state, email, phone, message

    Redirects:
        To the car detail page ('/cars/<car_id>') upon successful submission.
    """
    if request.method == 'POST':
        # Extract data from POST request
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message_content = request.POST['message']

        user_id = None # Initialize user_id
        if request.user.is_authenticated:
            user_id = request.user.id
            # Check if this authenticated user has already made an inquiry for this car
            if Contact.objects.filter(car_id=car_id, user_id=user_id).exists():
                messages.error(request, 'You have already inquired about this car. We will get back to you as soon as possible.')
                return redirect('/cars/' + car_id)

        # Create Contact object
        # Note: Storing 0 for user_id for non-authenticated users.
        # Consider using None if the database field allows NULL and it's more appropriate.
        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            user_id=user_id if user_id else 0,  # Assign 0 if user is not authenticated
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message_content
        )

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Car Inquiry',
                f'You have a new inquiry for the car: {car_title}. Please login to your admin panel for more info.',
                'brendaank2001@gmail.com', # Sender's email address
                [admin_email], # List of recipient email addresses
                fail_silently=False,
            )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/' + car_id)
    # Implicitly, if not POST, this view does nothing, which might be fine if only POST requests are routed.
    # Consider adding a redirect or error for GET requests if they are not intended.
