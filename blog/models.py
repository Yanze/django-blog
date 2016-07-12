from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()

    # this is a timezone-aware datetime.now
    publish = models.DateTimeField(default=timezone.now)

    # the date will be saved automatically when creating an object
    created = models.DateTimeField(auto_now_add=True)

    # date will be updated automatically when saving an object
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class meta:
        # tells Django to sort results with descending order by default
        ordering = ('-publish',)

    def __str__(self):
        # this is a default method human-readable representation of the object
        return self.title
