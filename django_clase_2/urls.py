from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", views.product_list, name="products_list"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
]
