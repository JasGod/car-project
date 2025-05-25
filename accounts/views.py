from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
Defines the views for the 'accounts' application.

This module contains view functions for user authentication processes
such as login, registration, logout, and a user dashboard.
It relies on Django's built-in authentication system and messages framework.
"""

def login(request):
    """
    Handles user login.

    If the request method is POST, it attempts to authenticate the user with
    the provided username and password. On successful authentication, the user
    is logged in and redirected to the 'dashboard'. If authentication fails,
    an error message is displayed, and the user is redirected back to the
    login page.

    If the request method is GET, it renders the login page.

    Renders:
        accounts/login.html
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in.')
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    """
    Handles user registration.

    If the request method is POST, it processes the registration form.
    It validates that the passwords match and checks if the username or email
    already exists. If validation is successful, a new user is created and
    logged in, then redirected to the 'dashboard'. If there are errors
    (password mismatch, existing username/email), appropriate error messages
    are displayed, and the user is redirected back to the registration page.

    If the request method is GET, it renders the registration page.

    Renders:
        accounts/register.html
    """
    if request.method == 'POST':
        # Extract form data
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exist!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exist!")
                return redirect('register')
            else:
                # Create new user
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                # user.save() is called by create_user, so the explicit user.save() below is redundant and unreachable.
                auth.login(request, user)
                messages.success(request, 'You are now registered and logged in.')
                return redirect('dashboard')
                # The following lines are unreachable due to the preceding redirect.
                # user.save()
                # messages.success(request,'You are registered successfully.')
                # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else: # GET request
        return render(request, 'accounts/register.html')

@login_required(login_url = 'login')
def dashboard(request):
    """
    Displays the user's dashboard.

    Requires the user to be logged in. Fetches and displays a list of
    inquiries made by the logged-in user, ordered by creation date (newest first).

    Renders:
        accounts/dashboard.html

    Context Variables:
        inquiries: QuerySet of Contact objects made by the current user.
    """
    user_inquiries = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries': user_inquiries,
    }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    """
    Handles user logout.

    If the request method is POST, the user is logged out.
    In either case (POST or any other method for robustness, though typically forms use POST),
    the user is then redirected to the 'home' page.

    Redirects:
        'home'
    """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('home')
    # For GET or other methods, also redirect to home, ensuring logout is attempted via POST.
    # Consider adding a message here if direct GET logout is not preferred.
    return redirect('home')
