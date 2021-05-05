from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('', views.CategoryTemplate.as_view()),
]