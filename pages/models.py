from django.db import models

# Create your models here.
"""
Defines the database models for the 'pages' application.

This module includes models for content that is primarily static or
informational, such as team member profiles.
"""

class Team(models.Model):
    """
    Represents a team member in the organization.

    Stores information about an individual team member, including their name,
    designation, photo, social media links, and when their profile was created.
    """
    first_name = models.CharField(max_length=255) # Team member's first name
    last_name = models.CharField(max_length=255) # Team member's last name
    designation = models.CharField(max_length=255) # Team member's role or designation
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/') # Photograph of the team member
    facebook_link = models.URLField(max_length=100) # URL to their Facebook profile
    twitter_link = models.URLField(max_length=100) # URL to their Twitter profile
    google_plus_link = models.URLField(max_length=100) # URL to their Google+ profile
    created_date = models.DateTimeField(auto_now_add=True) # Date the team member profile was created


    def __str__(self):
        """
        Returns a string representation of the team member.

        This is typically the team member's first name, used in the Django admin
        interface and other string representations of the model.
        """
        return self.first_name
