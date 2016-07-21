from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


"""
build-in syndication feed framework that we can use to dynamically
generate RSS or Atom feeds in a similar manner to creating sitemaps using
the sites framework
"""


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
