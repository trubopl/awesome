from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post


class StaticSitemap(Sitemap):

    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['index', 'generate', 'payday_loans', 'blog', 'first_free_loan']

    def location(self, item):
        return reverse(item)


class PostsSitemap(Sitemap):

    def items(self):
        return Post.objects.all()
