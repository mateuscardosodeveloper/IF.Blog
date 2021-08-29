from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog import models


def sample_user(email='test@email.com', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class BlogPostTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            'test2@email.com',
            'test123'
        )
        self.client.force_login(self.user)

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

    def test_retrieve_blog_post_list(self):
        """Test to retrieve a list of blog post"""
        models.BlogPost.objects.create(user=self.user, title='Hello There',
                                       slug='1', content='Hi')
        models.BlogPost.objects.create(user=self.user, title='Sunshine',
                                       slug='2', content='Summer amazing')

        response = self.client.get('/')

        blog_post = models.BlogPost.objects.all().order_by('-title')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(blog_post.count(), 2)

    def test_create_blog_post_successful(self):
        """Test to create a blog post with success"""
        payload = {
            'title': 'test',
            'slug': '1',
            'content': 'test content'
        }
        self.client.post('/blog-new/', payload)

        exists = models.BlogPost.objects.filter(
            user=self.user,
            title=payload['title']
        ).exists()
        self.assertTrue(exists)

    def test_create_post_blog_to_fail(self):
        """Test to create a blog post failed"""
        payload = {'title': ''}
        self.client.post('/blog-new/', payload)

        blog_post = models.BlogPost.objects.all().order_by('-title')
        self.assertEqual(blog_post.count(), 0)
