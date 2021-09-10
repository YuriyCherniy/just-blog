from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError

from .models import GuestPost, GuestComment, NewGuestPostCounter
from .forms import GuestCommentForm, GuestPostForm


class GuestPostList(ListView):
    model = GuestPost
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            post_counter = NewGuestPostCounter.objects.first()
            post_counter.reset_counter()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GuestPostForm()
        return context


class GuestPostDetail(LoginRequiredMixin, DetailView):
    model = GuestPost
    raise_exception = True


class GuestPostCreate(SuccessMessageMixin, CreateView):
    model = GuestPost
    fields = ['anonymous_username', 'text']
    success_url = reverse_lazy('guest_room')
    success_message = 'Сообщение добавлено'
    wrong_captcha = 'Системы безопасности сайта обнаружили подозрительную \
        активность с вашего IP адресса похожую на поведение ботов. \
        Попробуйте оставить сообщение ещё раз. Если проблема повторяется, \
        сообщите об этом администрации сайта.'

    def post(self, request, *args, **kwargs):
        form = GuestPostForm(request.POST)
        if form.is_valid():
            post_counter = NewGuestPostCounter.objects.first()
            post_counter.add_one()
            return super().post(request, *args, **kwargs)
        if form.errors.get('captcha', False):
            messages.warning(request, self.wrong_captcha)
        return render(
            request, 'guestroom/guestpost_form.html', {'form': form}
        )


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


class GuestCommentCreate(LoginRequiredMixin, SuccessMessageMixin, View):
    raise_exception = True

    def post(self, request):
        form = GuestCommentForm(request.POST)
        if form.is_valid():
            try:
                GuestComment.objects.create(
                    username=form.cleaned_data['username'],
                    text=form.cleaned_data['text'],
                    guest_post_id=form.cleaned_data['guest_post_pk']
                )
                messages.success(request, 'Комментарий добавлен')
            except IntegrityError:
                messages.warning(request, 'Это сообщение уже содержит комментарий')
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
