from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
"""
Defines the database models for the 'cars' application.

This module includes the `Car` model, which stores details about
the vehicles available in the car dealership.
"""

class Car(models.Model):
    """
    Represents a car listing in the database.

    Stores all relevant information about a vehicle, including its specifications,
    pricing, and dealership-specific details.
    """
    state_choice = (
        ('FR', 'France'),
        ('LI', 'Lituania'),
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    year_choice = []
    for r in range(2015, (datetime.now().year+1)):
        year_choice.append((r,r))


    features_choices = ( # Choices for car features
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = ( # Choices for number of doors
      ('2', '2'),
      ('3', '3'),
      ('4', '4'),
      ('5', '5'),
      ('6', '6'),
  )


    car_title = models.CharField(max_length=255) # Title of the car listing
    state = models.CharField(choices=state_choice, max_length=100) # State where the car is located
    city = models.CharField(max_length=100) # City where the car is located
    color = models.CharField(max_length=100) # Exterior color of the car
    model = models.CharField(max_length=100) # Model of the car (e.g., Camry, Civic)
    year = models.IntegerField(('year'), choices=year_choice) # Manufacturing year
    condition = models.CharField(max_length=100) # Condition (e.g., New, Used)
    price = models.IntegerField() # Price in the local currency
    description = RichTextField() # Detailed description, supports rich text
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/') # Main photo of the car
    car_photo_1  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Additional photo 1
    car_photo_2  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Additional photo 2
    car_photo_3  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Additional photo 3
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # Additional photo 4
    features = MultiSelectField(choices=features_choices) # Select multiple features
    body_style = models.CharField(max_length=100) # Body style (e.g., Sedan, SUV)
    engine = models.CharField(max_length=100) # Engine type or specification
    transmission = models.CharField(max_length=100) # Transmission type (e.g., Automatic, Manual)
    interior = models.CharField(max_length=100) # Interior color or material
    miles = models.IntegerField() # Number of miles driven (if used)
    doors = models.CharField(choices=door_choices, max_length=10) # Number of doors
    passengers = models.IntegerField() # Seating capacity
    vin_no = models.CharField(max_length=17) # Vehicle Identification Number
    milage = models.IntegerField() # Fuel efficiency (e.g., MPG or km/L)
    fuel_type = models.CharField(max_length=50) # Type of fuel (e.g., Petrol, Diesel, Electric)
    no_of_owners = models.CharField(max_length=100) # Number of previous owners
    is_featured = models.BooleanField(default=False) # Whether the car is a featured listing
    created_date = models.DateTimeField(default=datetime.now, blank=True) # Date when the listing was created


    def __str__(self):
        """
        Returns a string representation of the car model.

        This is typically the car's title, used in the Django admin interface
        and other string representations of the model.
        """
        return self.car_title
