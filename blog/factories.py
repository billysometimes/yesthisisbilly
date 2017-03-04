import factory
import factory.django

from .models import Post
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):

    username = factory.Sequence(lambda n: 'test_user_%s' % n)
    first_name = 'John'
    last_name = 'Doe'
    email = factory.LazyAttribute(lambda x: '%s@example.org' % x.username)
    is_superuser = False

    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

class PostFactory(factory.DjangoModelFactory):

    title = factory.Sequence(lambda n: 'Sample Title %s' % n)
    slug = factory.Sequence(lambda n: 'sample-slug-%s' % n)
    author = factory.SubFactory(UserFactory)
    body = factory.Sequence(lambda n: 'Sample text %s' % n)

    class Meta:
        model = Post
