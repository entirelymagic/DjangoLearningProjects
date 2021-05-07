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


# class CategoryTemplate(TemplateView):
#     template_name = "category.html"


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category_name = ''
    if category_slug:
        category_name = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_name)
    return render(request, 'product/product_list.html', {
        'products': products,
        'category': category_name,
        'categories': categories,
    })


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
