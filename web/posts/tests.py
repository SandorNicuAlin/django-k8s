from django.test import TestCase

from .models import Post

# Create your tests here.

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Hello World")
    
    def test_failure(self):
        qs = Post.objects.all()
        self.assertTrue(qs.exists())