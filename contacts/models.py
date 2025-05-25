from django.db import models
from datetime import datetime

# Create your models here.
"""
Defines the database models for the 'contacts' application.

This module includes the `Contact` model, which is used to store
user inquiries made about specific cars or general contact messages.
"""

class Contact(models.Model):
    """
    Represents a user inquiry or contact message.

    This model stores details submitted by users, typically through a contact
    form or an inquiry form related to a specific car. It captures user information,
    the subject of their inquiry (like a car they are interested in), and their message.
    """
    first_name = models.CharField(max_length=100) # Submitter's first name
    last_name = models.CharField(max_length=100) # Submitter's last name
    car_id = models.IntegerField() # ID of the car the inquiry is about, if applicable
    customer_need = models.CharField(max_length=100) # Type of inquiry (e.g., "Question", "Test Drive")
    car_title = models.CharField(max_length=100) # Title of the car the inquiry is about
    city = models.CharField(max_length=100) # Submitter's city
    state = models.CharField(max_length=100) # Submitter's state
    email = models.EmailField(max_length=100) # Submitter's email address
    phone = models.CharField(max_length=100) # Submitter's phone number
    message = models.TextField(blank=True) # The content of the user's message
    user_id = models.IntegerField(blank=True) # ID of the registered user, if the submitter is logged in
    create_date = models.DateTimeField(blank=True, default=datetime.now) # Timestamp of when the inquiry was created

    def __str__(self):
        """
        Returns a string representation of the contact inquiry.

        This is typically the submitter's email address, used in the Django admin
        interface and other string representations of the model.
        """
        return self.email
