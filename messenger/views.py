from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class IndexView(TemplateView):
    template_name = "index.html"
