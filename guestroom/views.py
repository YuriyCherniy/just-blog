from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import GuestPost, GuestComment
from .forms import GuestCommentForm


class GuestPostList(ListView):
    model = GuestPost
    paginate_by = 5


class GuestPostDetail(LoginRequiredMixin, DetailView):
    model = GuestPost
    raise_exception = True


class GuestPostCreate(SuccessMessageMixin, CreateView):
    model = GuestPost
    fields = ['anonymous_username', 'text']
    success_url = reverse_lazy('guest_room')
    success_message = 'Сообщение добавлено'


class GuestPostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GuestPost
    fields = ['anonymous_username', 'text']
    template_name = 'guestroom/guestpost_update_form.html'
    success_url = reverse_lazy('guest_room')
    raise_exception = True
    success_message = 'Сообщение обновлено'


class GuestPostDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = GuestPost
    success_url = reverse_lazy('guest_room')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Сообщение удалено')
        return super().post(request, *args, **kwargs)


class GuestCommentCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    raise_exception = True

    def post(self, request):
        form = GuestCommentForm(request.POST)
        if form.is_valid():
            GuestComment.objects.create(
                username=form.cleaned_data['username'],
                text=form.cleaned_data['text'],
                guest_post_id=form.cleaned_data['guest_post_pk']
            )
            messages.success(request, 'Комментарий добавлен')
            return redirect(reverse('guest_room'))

        messages.warning(request, 'Проверьте данные')
        return render(
            request, 'guestroom/guestcomment_form.html', {'form': form}
        )


class GuestCommentUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GuestComment
    fields = ['username', 'text']
    template_name = 'guestroom/guestcomment_update_form.html'
    success_url = reverse_lazy('guest_room')
    success_message = 'Комментарий обнавлён'
    raise_exception = True


class GuestCommentDelete(LoginRequiredMixin, DeleteView):
    model = GuestComment
    success_url = reverse_lazy('guest_room')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Комментарий удалён')
        return super().post(request, *args, **kwargs)
