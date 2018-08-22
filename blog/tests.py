import datetime
from django.test import TestCase
from django.utils import timezone


from .models import Post


class PostModelTests(TestCase):

    def test_was_published_in_the_past(self):
        """
        was_published_in_the_past() returns False for posts whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertIs(future_post.was_published_in_the_past(), False)