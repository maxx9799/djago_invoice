from os import name
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'myapi'

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/", views.detail, name="detail"),
    path("pdf/", views.render_pdf_view, name="pdf_view")
    
]

