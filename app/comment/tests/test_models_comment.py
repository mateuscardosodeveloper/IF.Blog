from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog import models
from comment.models import Comment


def sample_user(email='test@email.com', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user( email, password)


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


class ModelTestsComment(TestCase):

    def test_create_comment_str(self):
        """Test to create a comment with string representation"""

        user2 = get_user_model().objects.create_user(
            'test2'
            'test2@email.com',
            'test12345',
        )
        #import ipdb;ipdb.set_trace()
        comment = Comment.objects.create(
            user=sample_user(),
            blogpost=sample_blog_post(user=user2),
            comment='Test comment',
        )
        

        self.assertEqual(str(comment), comment.comment)
