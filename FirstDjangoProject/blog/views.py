from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.


def about(request):
    return HttpResponse("<h1>Hy there </h1>")


def add(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    c = int(request.GET.get('c'))
    return HttpResponse(f"The result is {a + b + c}")


def multiply(request, a, b, c):
    return HttpResponse(f"Result is {a, b, c}")


