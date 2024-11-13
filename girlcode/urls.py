"""
URL configuration for girlcode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

#for media files uploaded by users
from django.conf import settings
from django.conf.urls.static import static

#sitemaps
from django.contrib.sitemaps.views import sitemap 
from listings.sitemaps import PostSitemap

#Google Play Digital Assets Link
from girlcode.views import digital_assets

urlpatterns = [
    path('admin/', admin.site.urls),
    ## apps
    path("storytime/", include("listings.urls")),
    #path("girlchat/", include("girlchat.urls")),
    path('girlchat/', include('girlchat.urls', namespace='girlchat')),

    ## django allanauth
    path('accounts/', include('allauth.urls')),
    path("i18n/", include("django.conf.urls.i18n")), #internalization

    #django-pwa
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix

    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': {'post' : PostSitemap}}, 
     name='django.contrib.sitemaps.views.sitemap'),

    #google
    path("privacy", views.privacy, name="privacy"),
    path("app-ads.txt", views.appads, name="appads"),
    path("ads.txt", views.adsenseads, name="adsenseads"),

    #Google Play Digital Assets Link
    path(".well-known/assetlinks.json", digital_assets),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='storytime/', permanent=True)),
]