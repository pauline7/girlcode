from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap): 
    def items(self): 
        return Post.objects.all() 
        
    def lastmod(self, obj): 
        return obj.created

# class PackageSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.7
#     protocol = "https"

#     def items(self):
#        return Package.objects.filter('pub_date')
 
#     def lastmod(self, item): 
#        return item.created

# from listings.urls import urlpatterns as listingsUrls
# # from mathit.urls import urlpatterns as mathitUrls
# from django.core.urlresolvers import reverse

# class StaticSitemap(Sitemap):
#      priority = 0.8
#      changefreq = 'weekly'
#      protocol = "https"

#      # The below method returns all urls defined in urls.py file
#      def items(self):
#         mylist = [ ]
#         for url in listingsUrls:
#             mylist.append('listing:'+url.name) 
#         return mylist

#      def location(self, item):
#          return reverse(item)