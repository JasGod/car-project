# Live Website Content Summary: Carzone Project

This document provides a summary of the content and features observed on the live website deployed at: `https://secret-journey-08271-bc01b5bc2f46.herokuapp.com/`

The website appears to be a deployment of the "Carzone" car dealership project.

## Overall Purpose:
The website serves as an online portal for a car dealership. It allows users to browse, search, and find information about cars available for sale.

## Key Features and Content Sections:

1.  **Homepage/Landing Page:**
    *   **Contact Information:** Displays phone number, email, and operating hours prominently.
    *   **Navigation Menu:** Standard links including Home, Cars, About, Services, and Contact. It also includes User Account links (Login/Register).
    *   **Promotional Banners:** Features rotating banners with slogans related to finding a dream car.
    *   **Car Search Functionality:** A primary search form allowing users to search by criteria such as Model, Location, Year, and Type of Car, with an option to filter by Price.
    *   **Featured Cars Section:** Highlights specific vehicles with key details: price, images, name (e.g., "2018 Toyota Corolla"), location, and essential specifications (fuel type, mileage, transmission, body style, color, year). Each listing links to a more detailed page.
    *   **Latest Cars Section:** Similar to "Featured Cars," this area showcases recently added vehicles with their details and links.
    *   **"Executive Team" Section:** A brief section likely intended to introduce the dealership's team.
    *   **Call to Action for Inquiries:** A "Do You Have Questions ? Get in Touch" prompt, linking to the contact page.
    *   **Footer:** Contains copyright information ("© 2025 Carzone Corp.") and links to social media platforms.

2.  **Car Listings Page (`/cars/`):**
    *   While the homepage displays "Featured" and "Latest" cars, a dedicated `/cars/` page is available, presumably offering a comprehensive inventory with more advanced sorting and filtering capabilities.

3.  **Car Detail Pages (e.g., `/cars/<car_id>`):**
    *   Accessible by clicking on individual car listings.
    *   These pages provide extensive details about a specific car, including:
        *   Multiple photographs.
        *   A list of features (e.g., Cruise Control, Airbags, Air Conditioning).
        *   An overview section (Model, Year, Condition, Price).
        *   A descriptive text area (noted to contain placeholder "Lorem Ipsum" text in the fetched version).

4.  **User Accounts (`/accounts/login`, `/accounts/register`):**
    *   The site includes standard functionality for user registration and login.

5.  **Static/Informational Pages:**
    *   **About (`/about`):** Expected to contain information about the dealership and its team.
    *   **Services (`/services`):** Likely details the range of services offered by the dealership.
    *   **Contact (`/contact`):** Provides a way for users to send messages or inquiries to the dealership.

## Inferred Underlying Structure:
The URL patterns (e.g., `/cars/`, `/accounts/login`, `/media/photos/...`) and the overall layout strongly suggest that this live website is a deployment of the Django-based "CarWeb" project. The paths for images (`media/photos/2025/05/...`) are consistent with typical Django configurations for media files.

In summary, the website functions as a standard online platform for a car dealership, enabling customers to explore available vehicles and the business to showcase its inventory effectively.
