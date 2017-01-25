from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, User
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from messenger.models import Message
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['inbox'] = Message.objects.filter(recipient=self.request.user)
            return context


class MessageCreateView(CreateView):
    model = Message
    fields = ('recipient', "body",)
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
            instance = form.save(commit=False)
            instance.sender = self.request.user
            return super().form_valid(form)
