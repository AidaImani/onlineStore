from django.shortcuts import render, get_object_or_404,redirect,reverse
from cart.forms import CarAddProductForm
from .models import Product, Category
from django.db.models import Q


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/Products/list.html', {'category': category, 'categories': categories,
                                                       'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CarAddProductForm()
    return render(request, 'shop/Product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def about(request):
    return render(request, 'shop/aboutUs.html')


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        # submitbutton = request.GET.get('submit')
        try:
            if query is not None:
                lookups = Q(name__icontains=query)

                results = Product.objects.get(lookups)

                # context = {'results': results,
                #            'submitbutton': submitbutton,
                #            }

                return redirect(reverse('shop:product_detail', args=[results.id, results.slug]))

            # else:
            #     return render(request, 'shop/Products/list.html')

        except:
            return render(request, 'shop/Products/list.html')

    else:
        return render(request, 'shop/Products/list.html')
