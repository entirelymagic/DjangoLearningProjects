from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from . import views

urlpatterns = [
    path('categories', views.product_list),
    path('categories/<slug:category_slug>', views.product_list),
    path('', views.CategoryTemplate.as_view()),
]