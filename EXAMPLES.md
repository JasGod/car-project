# EXAMPLES.md

## Usage Examples for CarWeb Project

This document provides examples of how to interact with the CarWeb project components, primarily focusing on backend model interactions.

### 1. Working with Car Listings (Django Shell or Custom Scripts)

These examples demonstrate how to query and retrieve car information using the Django ORM. You can run these in the Django shell (`python manage.py shell`) or use them in your custom management commands or scripts.

First, ensure your Django environment is set up:
```python
import os
import django

# Replace 'carweb.settings' with your actual project settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carweb.settings')
django.setup()
```

Now, you can import and use your models:

```python
from cars.models import Car

# Get all cars
all_cars = Car.objects.all()
print(f"Found {all_cars.count()} cars.")
for car in all_cars:
    print(f"- {car.car_title} ({car.year}) - ${car.price}")

# Filter cars by make (e.g., 'Toyota')
# Assuming 'car_title' contains the make and model, or you have a specific 'make' field.
# This example assumes make is part of the title. Adjust if you have a dedicated 'make' field.
toyotas = Car.objects.filter(car_title__icontains='Toyota') # Example: 'Toyota Camry'
print(f"\nFound {toyotas.count()} Toyota cars.")
for car in toyotas:
    print(f"- {car.car_title}")

# Filter cars by model (e.g., 'Civic')
# The 'model' field directly stores the model name
civics = Car.objects.filter(model__iexact='Civic')
print(f"\nFound {civics.count()} Civic cars.")
for car in civics:
    print(f"- {car.car_title}")

# Filter cars by year
cars_from_2020 = Car.objects.filter(year=2020)
print(f"\nFound {cars_from_2020.count()} cars from 2020.")

# Get a specific car by its ID (e.g., ID=1)
try:
    specific_car = Car.objects.get(pk=1)
    print(f"\nDetails for car ID 1: {specific_car.car_title}")
    print(f"  Price: ${specific_car.price}")
    print(f"  Features: {specific_car.features}") # MultiSelectField
except Car.DoesNotExist:
    print("\nCar with ID 1 not found.")

# Accessing car attributes
if all_cars.exists():
    first_car = all_cars.first()
    print(f"\nAttributes of the first car ({first_car.car_title}):")
    print(f"  State: {first_car.state}")
    print(f"  Body Style: {first_car.body_style}")
    print(f"  Fuel Type: {first_car.fuel_type}")
    print(f"  Description: {first_car.description[:100]}...") # RichTextField, showing first 100 chars
```

### 2. Creating a Contact/Inquiry Programmatically

This shows how you might create a contact entry programmatically, for example, in a test script or a management command.

```python
from contacts.models import Contact
from django.utils import timezone
from django.contrib.auth.models import User # Assuming you might link to a User

# Ensure Django environment is set up if running standalone
# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carweb.settings')
# django.setup()

# Example data for a new contact message
user_id_example = None # Default to None for anonymous or if user doesn't exist
# Optionally, try to get an actual user
try:
    # Replace with an actual username or criteria to fetch a user
    test_user = User.objects.filter(is_superuser=False).first() 
    if test_user:
        user_id_example = test_user.id
except User.DoesNotExist:
    pass # Keep user_id_example as None or handle as 0 if your model uses that for anonymous

# Assuming a car with ID=1 exists for the inquiry
car_id_example = 1 
car_title_example = "Test Car for Inquiry" # Ideally fetch this from Car.objects.get(pk=car_id_example).car_title

try:
    # Check if the car exists
    from cars.models import Car
    if not Car.objects.filter(pk=car_id_example).exists():
        print(f"\nCar with ID {car_id_example} does not exist. Cannot create inquiry for it.")
    else:
        retrieved_car = Car.objects.get(pk=car_id_example)
        car_title_example = retrieved_car.car_title

        new_inquiry = Contact.objects.create(
            first_name="Jane",
            last_name="Developer",
            car_id=car_id_example, 
            customer_need="Technical Question",
            car_title=car_title_example, 
            city="Testville",
            state="TS", # Example state code
            email="jane.dev@example.com",
            phone="987-654-3210",
            message="This is a test inquiry created programmatically.",
            user_id=user_id_example, 
            # create_date defaults to datetime.now in the model, so explicitly setting it is optional
            # create_date=timezone.now() 
        )
        print(f"\nSuccessfully created inquiry from {new_inquiry.first_name} {new_inquiry.last_name} regarding '{new_inquiry.car_title}'.")
        print(f"Inquiry ID: {new_inquiry.id}")

except Car.DoesNotExist:
    print(f"\nCar with ID {car_id_example} not found. Cannot create inquiry.")
except Exception as e:
    print(f"\nError creating inquiry: {e}")
```

### 3. Typical End-User Interaction (Frontend Flow)

This section describes how an end-user would typically interact with the CarWeb application through their web browser.

1.  **Browsing Cars:**
    *   Users can navigate to the `/cars/` page (or the homepage which often lists cars) to see available vehicles.
    *   The listings usually display key information like car title, a primary image, price, and year.
    *   Pagination is used to manage large numbers of listings.

2.  **Searching and Filtering:**
    *   The car listings page (`/cars/`) and often the homepage include search and filter capabilities.
    *   Users can search by keywords (which might check the description, title, etc.).
    *   Filters allow users to narrow down results by criteria such as:
        *   Model (e.g., Camry, F-150)
        *   Location (City, State)
        *   Year of manufacture
        *   Body Style (e.g., Sedan, SUV, Truck)
        *   Price range

3.  **Viewing Car Details:**
    *   Clicking on a car listing takes the user to that car's detail page (e.g., `/cars/<id>/` where `<id>` is the car's unique identifier).
    *   This page shows comprehensive information: multiple photos, detailed specifications (engine, transmission, mileage, etc.), a list of features, and the full description.

4.  **User Accounts:**
    *   Users can register for a new account by navigating to `/accounts/register/`.
    *   Registered users can log in at `/accounts/login/`.
    *   Once logged in, users are typically redirected to a dashboard (`/accounts/dashboard/`) where they might view their past inquiries or other personalized information.
    *   Logout functionality is also provided.
    *   The site may also support social authentication (e.g., Google, Facebook).

5.  **Making an Inquiry/Contacting:**
    *   From a car detail page, users can submit an inquiry form specific to that car. This form usually pre-fills some car details.
    *   A general contact page (e.g., `/contact/` or a similar link in `pages` app) is available for general questions or feedback.
    *   Users fill out the form with their name, email, phone, and message. The system saves this inquiry and typically notifies the dealership staff.

These examples should provide a good starting point for developers to understand backend operations and for any user to understand the application's flow.

---
*Note: The Django setup code at the beginning of script examples is crucial for running them outside of `python manage.py shell` or a Django-managed command.*
