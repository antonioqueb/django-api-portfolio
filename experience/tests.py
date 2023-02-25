from django.test import TestCase
from .models import Experience
from datetime import datetime

class ExperienceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Experience.objects.create(
            position="Software Developer",
            company="ABC Company",
            startDate=datetime.strptime('2022-01-01', '%Y-%m-%d').date(),
            endDate=datetime.strptime('2022-06-30', '%Y-%m-%d').date(),
            logoUrl='static/logos/company/abc.png'
        )

    def test_company_name_label(self):
        experience = Experience.objects.get(id=1)
        field_label = experience._meta.get_field('company').verbose_name
        self.assertEqual(field_label, 'company')

    def test_position_max_length(self):
        experience = Experience.objects.get(id=1)
        max_length = experience._meta.get_field('position').max_length
        self.assertEqual(max_length, 50)

    def test_logoUrl_upload_to(self):
        experience = Experience.objects.get(id=1)
        upload_to = experience._meta.get_field('logoUrl').upload_to
        self.assertEqual(upload_to, 'static/logos/company')

    def test_experience_model_str(self):
        experience = Experience.objects.get(id=1)
        self.assertEqual(str(experience), "ABC Company")

    def test_experience_start_date_not_null(self):
        experience = Experience.objects.get(id=1)
        field = experience._meta.get_field('startDate')
        self.assertFalse(field.null)

    def test_experience_end_date_not_null(self):
        experience = Experience.objects.get(id=1)
        field = experience._meta.get_field('endDate')
        self.assertFalse(field.null)

    def test_end_date_after_start_date(self):
        experience = Experience.objects.get(id=1)
        self.assertTrue(experience.endDate > experience.startDate)
