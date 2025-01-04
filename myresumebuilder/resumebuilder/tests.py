from django.test import TestCase
from django.urls import reverse
from .models import Resume, CountryCode


# Create your tests here.
class ModelsTestCase(TestCase):
    def setUp(self):
        self.country_code = CountryCode.objects.create(code="US", country="United States")
        self.resume = Resume.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            education="Some University",
            work_experience="Some Company",
            country_code=self.country_code,
            phone_number="1234567890",
            summary="Experienced professional",
            skills="Python, Django",
            certifications="CertA, CertB",
            projects="ProjectA, ProjectB",
            languages="English, Cantonese",
            hobbies="Reading, Cooking"
        )

    def test_country_code_str(self):
        self.assertEqual(str(self.country_code), "United States US")

    def test_resume_str(self):
        self.assertEqual(str(self.resume), "John Doe's Resume")

    def test_resume_created_at(self):
        self.assertIsNotNone(self.resume.created_at)

    def test_resume_updated_at(self):
        self.assertIsNotNone(self.resume.updated_at)


class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello, world. You're at the resume builder index.")

class LandingPageViewTest(TestCase):
    def test_landing_page_status_code(self):
        """Test if the landing page returns a 200 status code."""
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)

    def test_landing_page_template(self):
        """Test if the correct template is used for the landing page."""
        response = self.client.get(reverse('landing_page'))
        self.assertTemplateUsed(response, 'resumebuilder/landing_page.html')

    def test_landing_page_content(self):
        """Test if the landing page contains specific content."""
        response = self.client.get(reverse('landing_page'))
        self.assertContains(response, 'Welcome to My Resume Builder')
        self.assertContains(response, 'Start building your resume now!')
        self.assertContains(response, 'Go to Resume Builder')