from django.shortcuts import render, get_object_or_404

from store_app.models import Product


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", context={"product": product})


