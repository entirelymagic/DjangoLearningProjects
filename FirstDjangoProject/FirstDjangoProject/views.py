from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'


def welcome(request):
    return render(request, "home.html")


class BlogPageView(TemplateView):
    template_name = 'blog.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class HelloGreetTemplate(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = {'username': kwargs['name']}
        return context


def render_templates(request, template):
    return render(request, f"{template}")