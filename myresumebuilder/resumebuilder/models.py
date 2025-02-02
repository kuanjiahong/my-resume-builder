from django.db import models


class CountryCode(models.Model):
    code = models.CharField(max_length=5)
    country = models.CharField(max_length=50)

    # Reference: https://stackoverflow.com/questions/43865989/unresolved-attribute-reference-objects-for-class-in-pycharm
    objects = models.Manager()

    def __str__(self):
        return f"{self.country} {self.code}"


# Create your models here.
class Resume(models.Model):

    # Reference: https://stackoverflow.com/questions/43865989/unresolved-attribute-reference-objects-for-class-in-pycharm
    objects = models.Manager()

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
