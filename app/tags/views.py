from django.views.generic import ListView

from tags.models import Tag


class PostListFromTag(ListView):
    paginate_by = 10
    template_name = 'tags/tags_post_list.html'

    def get_queryset(self):
        qs = Tag.objects.get(slug=self.kwargs['slug']).post_set.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['slug']
        return context
