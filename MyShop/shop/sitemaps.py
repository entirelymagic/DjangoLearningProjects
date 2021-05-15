from django.contrib.sitemaps import Sitemap
from .models import Product


class ProductsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated
