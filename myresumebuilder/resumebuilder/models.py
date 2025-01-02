from django.db import models

# Create your models here.
class Resume(models.Model):
    # Required
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    education = models.TextField()
    work_experience = models.TextField()
    country_code = models.ForeignKey(CountryCode, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    # Optional
    summary = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Resume"


