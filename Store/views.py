from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from Store.models import category 
from Store.models import product
from django.http import HttpResponse
# Create your views here.


class page(View):
     def store(request):
    #     cart = request.session.get('cart')
    #     if not cart:
    #         request.session['cart'] = {}
    #     products = None
    #     categories = category.objects.all()
    #     categoryId = request.GET('category')
    #     if categoryId:
    #          products = product.objects.filter(category = categoryId)
    #     else:
    #          products = product.objects.all()

    #     data = {}
    #     data['products'] = products
    #     data['categories'] = categories
        return render(request, 'templates/base.html', data)