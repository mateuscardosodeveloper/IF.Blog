from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone
from blog import models
from comment.models import Comment


def sample_user(email='test@email.com', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def sample_blog_post(user, **params):
    """Create and return sample ativos"""
    defaults = {
        'title': 'test blog post',
        'slug': 'test',
        'content': 'content test',
        'publish_date': timezone.now()
    }
    defaults.update(params)

    return models.BlogPost.objects.create(user=user, **defaults)


class TestsComment(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            'test2@email.com',
            'test123'
        )
        self.client.force_login(self.user)

    def test_create_comment_str(self):
        """Test to create a comment with string representation"""
        user2 = get_user_model().objects.create_user(
            'test2'
            'test2@email.com',
            'test12345',
        )
        comment = Comment.objects.create(
            user=sample_user(),
            blogpost=sample_blog_post(user=user2),
            comment='Test comment',
        )

        self.assertEqual(str(comment), comment.comment)

    def test_retrieve_comment_list(self):
        """Test to retrieve a list comment"""
        Comment.objects.create(user=self.user, comment="Whats's up!?")
        Comment.objects.create(user=self.user, comment="How are you?")

        response = self.client.get('/')

        blog_post = Comment.objects.all().order_by('-comment')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(blog_post.count(), 2)

    def test_create_comment_successful(self):
        """Test to create a comment with success"""
        payload = {
            'blogpost': sample_blog_post(user=self.user),
            'comment': 'So funny'
        }

        self.client.post('/blog/test/comment/', payload)

        exists = Comment.objects.filter(
            user=self.user,
            comment=payload['comment']
        ).exists()
        self.assertTrue(exists)

    def test_create_comment_to_fail(self):
        """Test to create a comment failed"""
        payload = {
            'blogpost': sample_blog_post(user=self.user),
            'comment': ''
        }
        self.client.post('/blog/test/comment/', payload)

        comment = Comment.objects.all().order_by('-comment')
        self.assertEqual(comment.count(), 0)
