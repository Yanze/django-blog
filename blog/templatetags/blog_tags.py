from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

"""
each template tags module need to contain a variable called 'register' to be
a valid tag Library.

this variable is an instance of template.Library and it's used to register
you own template tags and filters.


*** the power of custom template tags is that you can process ant data
and add it to any template regardless of the view executed.
You can perform querySet or process any data to display results
in your template
"""
register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=2):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_most_commented_posts(count=3):
    return Post.published.annotate(total_comments=Count('comments'))\
                                    .order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
