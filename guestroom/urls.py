from django.urls import path

from .views import (GuestCommentCreate, GuestCommentDelete, GuestCommentUpdate,
                    GuestPostCreate, GuestPostDelete, GuestPostDetail,
                    GuestPostList, GuestPostUpdate)

urlpatterns = [
    path('', GuestPostList.as_view(), name='guest_room'),
    path('create-guest-post', GuestPostCreate.as_view(), name='guest_post_create'),
    path('update-guest-post-<int:pk>', GuestPostUpdate.as_view(), name='guest_post_update'),
    path('delete-guest-post-<int:pk>', GuestPostDelete.as_view(), name='guest_post_delete'),
    path('guest-post-<int:pk>', GuestPostDetail.as_view(), name='guest_post_detail'),

    path('create-guest-comment', GuestCommentCreate.as_view(), name='guest_comment_create'),
    path('delete-guest-comment-<int:pk>', GuestCommentDelete.as_view(), name='guest_comment_delete'),
    path('update-guest-comment-<int:pk>', GuestCommentUpdate.as_view(), name='guest_comment_update'),
]
