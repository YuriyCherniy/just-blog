from django.urls import path

from tags.views import PostListFromTag

urlpatterns = [
    path('<str:slug>', PostListFromTag.as_view(), name='post_from_tag')
]
