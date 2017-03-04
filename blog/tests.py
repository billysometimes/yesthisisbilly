from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from datetime import datetime

class PostTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(first_name="Super", last_name="User", username="superuser", is_superuser=True)
        Post.objects.create(title="PostTitle", author=user)

    def test_post_default_publish_date(self):
        post = Post.objects.get(title="PostTitle")
        assert post.publish_date.date() == datetime.today().date()
