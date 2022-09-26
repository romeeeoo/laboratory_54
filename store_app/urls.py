from django.urls import path
from store_app.views import index_view, product_view, categories_add_view, add_product_view

urlpatterns = [
    path('', index_view, name='home'),
    path('products/', index_view),
    path('products/<int:pk>', product_view, name='product_detailed'),
    path('categories/add', categories_add_view, name='add_new_category'),
    path('products/add/', add_product_view, name='add_new_product')
]
