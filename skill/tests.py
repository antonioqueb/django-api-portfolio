from django.test import TestCase
from .models import Skill

class SkillModelTestCase(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name="Python",
            logo_url="static/logos/skill/python.png",
            experience="3 years"
        )

    def test_skill_creation(self):
        self.assertTrue(isinstance(self.skill, Skill))
        self.assertEqual(self.skill.__str__(), self.skill.name)

    def test_skill_name(self):
        self.assertEqual(self.skill.name, "Python")

    def test_skill_logo_url(self):
        self.assertEqual(self.skill.logo_url, "static/logos/skill/python.png")

    def test_skill_experience(self):
        self.assertEqual(self.skill.experience, "3 years")

    def test_skill_name_max_length(self):
        max_length = self.skill._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_skill_logo_url_upload_to(self):
        upload_to = self.skill._meta.get_field('logo_url').upload_to
        self.assertEqual(upload_to, "static/logos/skill")

    def test_skill_experience_max_length(self):
        max_length = self.skill._meta.get_field('experience').max_length
        self.assertEqual(max_length, 200)
