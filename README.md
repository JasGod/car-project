# CarWeb - Car Dealership Web Application

## Project Description
CarWeb is a comprehensive web application designed for car dealerships. It enables users to browse through a wide variety of car listings, search for specific vehicles based on multiple criteria, manage their user accounts, and easily contact the dealership for inquiries or support. The platform aims to provide a seamless and user-friendly experience for both customers looking for cars and dealership staff managing the inventory and customer interactions.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd carweb
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Dependencies
The project dependencies are listed in the `requirements.txt` file. Key dependencies include:
- Django (Web framework)
- django-allauth (Authentication and social account management)
- django-ckeditor (Rich text editor)
- gunicorn (WSGI HTTP Server for UNIX)
- psycopg2-binary (PostgreSQL adapter for Python)
- Pillow (Python Imaging Library for image processing)

For a full list, please see the `requirements.txt` file.

## Deployment Environment Requirements
- Python 3.13.3 (as specified in `runtime.txt`)
- PostgreSQL (or other Django-compatible database, PostgreSQL is configured by default)
- Web server (e.g., Gunicorn, Nginx)

## How to Run the Application Locally
1. Ensure all dependencies are installed and migrations are applied as per the Installation Instructions.
2. Start the development server:
   ```bash
   python manage.py runserver
   ```
3. Open your web browser and navigate to `http://127.0.0.1:8000/`

## API Documentation
This project uses Sphinx to generate API documentation from docstrings.
To build the HTML documentation:
1. Ensure Sphinx is installed: `pip install Sphinx sphinx-rtd-theme` (or via `requirements.txt`)
2. Navigate to the `docs` directory: `cd docs`
3. Build the HTML: `make html` (or `sphinx-build -b html . _build/html` if make is not available)
4. Open `_build/html/index.html` in your browser.
