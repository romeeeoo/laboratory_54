from django.urls import path
from store_app.views import index_view, product_view

urlpatterns = [
    path('', index_view, name='home'),
    path('products/', index_view),
    path('products/<int:pk>', product_view, name='product_detailed')
]
