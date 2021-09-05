from django.urls import path

from .views import PostDetail


urlpatterns = [
    path('<str:slug>', PostDetail.as_view(), name='post_detail')
]
