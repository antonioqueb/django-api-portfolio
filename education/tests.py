from django.test import TestCase
from .models import Education

class EducationModelTestCase(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            degree="Bachelor's degree in Computer Science",
            institution="Example University",
            start_date="2017",
            end_date="2021",
            logo_url="https://example.com/logo.png",
            website_url="https://example.com",
        )

    def test_education_creation(self):
        education = Education.objects.create(
            degree="Master's degree in Data Science",
            institution="Another University",
            start_date="2022",
            end_date="2024",
            logo_url="https://anotherexample.com/logo.png",
            website_url="https://anotherexample.com",
        )
        self.assertTrue(isinstance(education, Education))
        self.assertEqual(education.__str__(), education.degree + " at " + education.institution)

    def test_education_degree(self):
        self.assertEqual(self.education.degree, "Bachelor's degree in Computer Science")

    def test_education_institution(self):
        self.assertEqual(self.education.institution, "Example University")

    def test_education_start_date(self):
        self.assertEqual(self.education.start_date, "2017")

    def test_education_end_date(self):
        self.assertEqual(self.education.end_date, "2021")

    def test_education_logo_url(self):
        self.assertEqual(self.education.logo_url, "https://example.com/logo.png")

    def test_education_website_url(self):
        self.assertEqual(self.education.website_url, "https://example.com")
