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


class IndexView(ListView):
    template_name = "index.html"
    queryset = Message.objects.all()


class MessageCreateView(CreateView):
    model = Message
    fields = ('recipient', "body",)
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
            instance = form.save(commit=False)
            instance.sender = self.request.user
            return super().form_valid(form)
