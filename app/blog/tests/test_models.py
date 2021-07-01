from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog import models




def sample_user(username='test', email='test@email.com', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(username, email, password)


class ModelTests(TestCase):
    
    def test_create_blog_post_str(self):
        """Test to create a blog post with a string representation"""
        blog_post = models.BlogPost.objects.create(
            user=sample_user(),
            title='test blog post',
            slug='test',
            content='content test',
            publish_date=timezone.now()
        )

        self.assertEqual(str(blog_post), blog_post.title)
