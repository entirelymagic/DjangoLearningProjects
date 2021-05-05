from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import View, ListView
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.all()


class CategoryTemplate(TemplateView):
    template_name = "category.html"



