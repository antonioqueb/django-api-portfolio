from django.test import TestCase
from .models import BlogPost, BlogImage, Comment

class BlogPostModelTestCase(TestCase):
    def setUp(self):
        self.comment1 = Comment.objects.create(
            name="John",
            email="john@example.com",
            content="This is a comment on the example post"
        )
        self.comment2 = Comment.objects.create(
            name="Jane",
            email="jane@example.com",
            content="This is another comment on the example post"
        )
        self.post = BlogPost.objects.create(
            title="Example post",
            content="This is an example blog post",
            hashtags="#example #blog #django",
            tags="example, blog, django",
            image_url="static/logos/default_image.png"
        )
        self.post.comments.add(self.comment1, self.comment2)
        self.image1 = BlogImage.objects.create(
            post=self.post,
            image="static/blog_images/example_image1.png"
        )
        self.image2 = BlogImage.objects.create(
            post=self.post,
            image="static/blog_images/example_image2.png"
        )

    def test_post_creation(self):
        post = BlogPost.objects.create(
            title="Another post",
            content="This is another blog post",
            hashtags="#another #blog #django",
            tags="another, blog, django",
            image_url="static/logos/default_image.png"
        )
        self.assertTrue(isinstance(post, BlogPost))
        self.assertEqual(post.__str__(), post.title)

    def test_post_title(self):
        self.assertEqual(self.post.title, "Example post")

    def test_post_content(self):
        self.assertEqual(self.post.content, "This is an example blog post")

    def test_post_hashtags(self):
        self.assertEqual(self.post.hashtags, "#example #blog #django")

    def test_post_tags(self):
        self.assertEqual(self.post.tags, "example, blog, django")

    def test_post_image_url(self):
        self.assertEqual(self.post.image_url, "static/logos/default_image.png")

    def test_post_comments(self):
        self.assertEqual(self.post.comments.count(), 2)

    def test_post_images(self):
        self.assertEqual(self.post.blogimage_set.count(), 2)
