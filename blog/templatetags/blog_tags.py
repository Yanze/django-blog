from django import template
from ..models import Post

"""
each template tags module need to contain a variable called 'register' to be
a valid tag Library.

this variable is an instance of template.Library and it's used to register
you own template tags and filters.
"""
register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()
