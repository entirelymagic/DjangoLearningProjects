from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect

from . import views

urlpatterns = [
    path('doc/', lambda request: HttpResponseRedirect('https://www.djangoproject.com/')),
    path('hello/', lambda request: HttpResponse("How are you? ")),
    path('about/', views.about),
    path("add/", views.add),
    path('multiply/<int:a>/<int:b>/<int:c>', views.multiply),
    path('reversed/<str:str_name>', views.reversed_string),

]
