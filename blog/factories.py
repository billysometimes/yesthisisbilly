import factory
import factory.django

from .models import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'A title'

    slug = 'a-slug'

    body = 'This is a body.'
