from django.views.generic import DetailView

from .models import Post


class PostDetail(DetailView):
    model = Post
