from django.urls import path,include
from firstweb.views import app_home

urlpatterns = [
    path('',app_home,name="app Home page")
]