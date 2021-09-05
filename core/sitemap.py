from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from posts.models import Post


class IndexSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class PostSiteMap(Sitemap):
    changefreq = 'yearly'
    priority = 0.6

    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.last_modified


class PostAboutSiteMap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)


class GuestRoomSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return ['guest_room']

    def location(self, item):
        return reverse(item)
