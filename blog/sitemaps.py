from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    """
    is a method that returns a list of objects. The objects retured will
    get passed to any callable methods corresponding to a sitemap property.
    """
    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish
