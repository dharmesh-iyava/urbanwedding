from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'home.html')
    
class homeView(ListView):
    model = Product
    template_name = 'caterer.html'


class catererView(DetailView):
    model = Product
    template_name = 'catererproduct.html'


"""def home(request):
    product = Product.objects.all()

    context = {'product': product}
    return render(request, 'home.html', context)


def caterer(request):
    return render(request, 'product.html')"""
