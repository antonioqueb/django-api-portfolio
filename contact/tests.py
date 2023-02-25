from django.test import TestCase
from .models import Contact

class ContactModelTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            email="test@example.com",
            phone_number=123456789,
            linkedin_url="https://www.linkedin.com/in/test/",
            github_url="https://github.com/test"
        )

    def test_email_field(self):
        field = self.contact._meta.get_field('email')
        self.assertEqual(field.verbose_name, 'email')
        self.assertEqual(field.max_length, 254)

    def test_phone_number_field(self):
        field = self.contact._meta.get_field('phone_number')
        self.assertEqual(field.verbose_name, 'phone number')
        self.assertEqual(field.get_internal_type(), 'IntegerField')

    def test_linkedin_url_field(self):
        field = self.contact._meta.get_field('linkedin_url')
        self.assertEqual(field.verbose_name, 'linkedin url')
        self.assertEqual(field.max_length, 50)

    def test_github_url_field(self):
        field = self.contact._meta.get_field('github_url')
        self.assertEqual(field.verbose_name, 'github url')
        self.assertEqual(field.max_length, 50)

    def test_email_label(self):
        field_label = self.contact._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_phone_number_label(self):
        field_label = self.contact._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_object_name_is_email(self):
        expected_object_name = self.contact.email
        self.assertEqual(expected_object_name, str(self.contact))
