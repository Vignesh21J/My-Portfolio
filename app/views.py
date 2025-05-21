from django.shortcuts import render, redirect
from .models import Home, Profiles, About, AboutProfile, Skill, Achievement, Portfolio

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from .models import ContactFormLog
from django.conf import settings


# Create your views here.
def home(request):
    home_data = Home.objects.first()
    home_profiles = Profiles.objects.filter(home=home_data)
    roles = home_data.get_roles_list() if home_data else []

    about_data = About.objects.first()
    about_profiles = AboutProfile.objects.all() if about_data else []

    skills = Skill.objects.all()[:10]
    half = len(skills) // 2

    portfolios = Portfolio.objects.all()
    achievements = Achievement.objects.all()

    context = {
        'home': home_data,
        'profiles': home_profiles,      # Social links for home
        'roles': roles,

        'about': about_data,            # Now this is a single object
        'about_profiles': about_profiles,  # For social links under About

        'left_skills': skills[:half],
        'right_skills': skills[half:],
        'portfolios': portfolios,
        'achievements': achievements,
    }
    return render(request, "index.html", context)



def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('user_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Simple form validation
        if not all([name, email, subject, message]):
            messages.error(request, "Please fill in all the fields.")
            return redirect('home')  # Redirect back to home if fields are missing

        # Prepare context for email
        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        html_content = render_to_string('email.html', context)

        is_success = False
        is_error = False
        error_message = ""

        try:
            send_mail(
                subject=subject,
                message=None,  # No plain message, HTML content will be sent
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request, "There's an error occurred, please try again later.")
        else:
            is_success = True
            messages.success(request, "Your email has been sent successfully!")

        # Log the form submission, whether successful or not
        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_error=is_error,
            is_success=is_success,
            error_message=error_message,
        )

    return redirect('home')
