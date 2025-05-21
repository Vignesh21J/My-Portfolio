from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=20)

    # Store multiple roles as a comma-separated string
    myroles = models.TextField(help_text="Add roles separated by commas (e.g., Software Developer, Web Developer)")

    picture = models.ImageField(upload_to='home/pictures/')
    updated = models.DateTimeField(auto_now=True)  # Ensure this field exists

    def __str__(self):
        return f'{self.id}. {self.name}'
    
    def get_roles_list(self):
        return [role.strip() for role in self.myroles.split(',') if role.strip()]  # For dynamic JS typing
    
    class Meta:
        ordering = ['-updated']
        verbose_name = "Home Section"
        verbose_name_plural = "Home Section"

    
class Profiles(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)
    icon_class = models.CharField(max_length=50, default='')  # For storing icon class.
    
    def __str__(self):
        return f"{self.social_name}"
    
    class Meta:
        verbose_name = "Social Profile"
        verbose_name_plural = "Social Profiles"
    



class About(models.Model):
    heading = models.CharField(max_length=60)  # I am Vignesh J [Learn!Pract!Imple] + resume's summary
    career = models.CharField(max_length=300)
    description = models.TextField(blank=False)  # About Me Description 
    profile_img = models.ImageField(upload_to='about/profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career
    
    class Meta:
        ordering = ['-updated']
        verbose_name = "About Section"
        verbose_name_plural = "About Section"



class AboutProfile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_profiles')
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)
    icon_class = models.CharField(max_length=50, default='')  # For storing icon class.

    def __str__(self):
        return self.social_name
    
    class Meta:
        verbose_name = "About Profile"
        verbose_name_plural = "About Profiles"




class Skill(models.Model):
    name = models.CharField(max_length=60)  # e.g., "HTML", "CSS", "JAVASCRIPT"
    value = models.PositiveIntegerField(default=0)  # e.g., 90 for 90%
    is_left = models.BooleanField(default=True)  # Show on left or right column

    def __str__(self):
        return f"{self.name} - {self.value}%"
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"




class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    icon_class = models.CharField(
        max_length=100,
        help_text="Example: bi bi-award, bi bi-trophy, bi bi-database-check"
    )
    
    icon_color = models.CharField(
        max_length=20,
        default="#ffc107",
        help_text="Hex color like #ffc107, #28a745, #17a2b8"
    )

    year = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="Example: 2025 (optional)"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
    


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'
    
    class Meta:
        verbose_name = "Portfolio Project"
        verbose_name_plural = "Portfolio Projects"



class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null = True, blank = True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)

    error_message = models.TextField(null = True,  blank = True)

    def __str__(self):
        return self.email