from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            date="2022-02-25",
            demo_url="https://example.com",
            github_url="https://github.com/example",
            details="Test project details",
            technologies=["Django", "React"],
            languages=["Python", "JavaScript"],
            image_url="test_image.jpg"
        )

    def test_project_title(self):
        self.assertEqual(self.project.title, "Test Project")

    def test_project_date(self):
        self.assertEqual(self.project.date, "2022-02-25")

    def test_project_demo_url(self):
        self.assertEqual(self.project.demo_url, "https://example.com")

    def test_project_github_url(self):
        self.assertEqual(self.project.github_url, "https://github.com/example")

    def test_project_details(self):
        self.assertEqual(self.project.details, "Test project details")

    def test_project_technologies(self):
        self.assertListEqual(self.project.technologies, ["Django", "React"])

    def test_project_languages(self):
        self.assertListEqual(self.project.languages, ["Python", "JavaScript"])
