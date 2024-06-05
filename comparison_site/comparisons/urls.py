from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_comparison_table, name='create_comparison_table'),
]
