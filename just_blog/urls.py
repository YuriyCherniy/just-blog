"""just_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from posts.views import PostDetailAbout
from core.sitemap import IndexSiteMap, PostSiteMap, PostAboutSiteMap, GuestRoomSiteMap


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('post/', include('posts.urls')),
    path('tag/', include('tags.urls')),
    path('about/', PostDetailAbout.as_view(), name='about'),
    path('guest-room/', include('guestroom.urls')),
    path(
        'sitemap.xml', sitemap,
        {'sitemaps': {'index': IndexSiteMap(), 'post': PostSiteMap(),
         'guest_room': GuestRoomSiteMap(), 'post_about': PostAboutSiteMap()}},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
