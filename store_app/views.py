from django.shortcuts import render, get_object_or_404, redirect

from store_app.models import Product, Category


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def categories_add_view(request):
    if request.method == 'GET':
        return render(request, 'category_add.html')
    elif request.method == 'POST':
        category_data = {'name': request.POST.get('name'),
                         'description': request.POST.get('description')
                         }
        Category.objects.create(**category_data)
        return redirect('home')
