from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Tag(models.Model):
    word        = models.CharField(max_length=35)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class PostTags(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)
