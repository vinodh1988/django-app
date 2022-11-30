from django.urls import path,include
from firstapi.apiviews import ProductAPI

urlpatterns = [
    path('/products',ProductAPI.as_view(),name="app Home page")
]