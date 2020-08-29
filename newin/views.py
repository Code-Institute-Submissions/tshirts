from django.shortcuts import render
from .models import Product

# Create your views here.
def all_newin(request):
    newin= Product.objects.all()
    return render(request, "newin.html", {"newin": newin})
    
