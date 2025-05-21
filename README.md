# My Portfolio Website - Django 5.1

This is my personal portfolio website built with *Django 5.1*. It highlights my skills, projects, and other details about myself. This site also includes a contact form that allows users to reach out to me via email.

## Features

- *Home Section*: A simple, clean introduction with a personal picture.
- *About Section*: A brief overview of my background, education, and career journey.
- *Skills Section*: Organized skills into categories as a tech stack domain.
 - *Achievement Section*: Organized my achievements as in a order wise.
- *Projects*: A showcase of projects with descriptions and links to repositories or live demos.
- *Contact Form*: Users can send me a message directly via email, which I will receive on my end. The form uses Django's email functionality for sending messages.
- *Responsive Design*: The website is responsive and works seamlessly across desktop and mobile devices.

## Technologies Used

- *Django 5.1*: A Python-based web framework for backend development.
- *HTML, CSS, JavaScript*: For frontend design and user interactivity.
- *Bootstrap*: For Full Responsive across various devices.
- *Django Email*: To handle the contact form and send messages to my email.
- *SQLite*: For database management (used for the contact form, etc.).

## Installation

Follow these steps to set up the project locally:

1. *Clone the repository*:
    bash
    git clone https://github.com/Vignesh21J/My-Portfolio.git
    cd My-Portfolio
    

2. *Create a virtual environment* (optional but recommended):
    bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    

3. *Install required dependencies*:
    bash
    pip install -r requirements.txt
    

4. *Set up email configuration* (optional):
    - Make sure you configure the email backend in settings.py for the email sending functionality. Update your email provider settings as needed.

5. *Apply migrations*:
    bash
    python manage.py migrate
    

6. *Run the development server*:
    bash
    python manage.py runserver
    

7. Open a browser and visit http://127.0.0.1:8000/ to see your portfolio website live.

## Contact Form Configuration

To enable the email functionality, configure the email settings in Django's settings.py file. Here’s an example configuration:

python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email service provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

Make sure to replace the placeholder values with your actual email credentials.
