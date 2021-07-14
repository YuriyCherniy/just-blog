from django.views.generic import DetailView

from .models import Post, PostAbout


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_list = self.object.tag.all()
        context['tag_list'] = tag_list
        return context


class PostDeatailAbout(DetailView):
    template_name = 'posts/post_detail_about.html'

    def get_object(self):
        obj = PostAbout.objects.first()
        return obj
