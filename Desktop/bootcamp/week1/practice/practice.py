from application.cart.models import Cart
from django.db.models import Q
from django.views.generic. import ListView, DetailView
from django.shortcuts import render, get_object_ot_404
from django.http import Http404
from .models import Product


class ProductDetailSlugView(DetailView):
queryset = Product.objects.all()
template_name = 'products/detail.html'

def get_context_data(self, *args, **kwargs):
    context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
    cart_obj, new_obj = Cart.bjects.get_or_new(self.requests)
    context['carts'] = cart_obj
    return context

    def get_object(self, *args, **kwargs):
        request = self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
            except Product.DoesNotExist:
                raise Http404("Not Found ...")
            except Product.MultipleObjectsReturned:
                qs = Product.objects.filter(slug=slug, active=True)
                instance = qs.first()
            except:
                raise Http404("MMMM")
                return instance


class ProductFeaturedListView(ListView):
    queryset = Product.objects.featured()
    template_name = 'product/list.html'

    #def get_queryset(self, *args, **kwargs):
    #    request = self.request
    #    return Product.objects.featured()

















    class Product