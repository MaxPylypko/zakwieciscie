from django.shortcuts import render

# Create your views here.
def item(request):
    return render(request, "catalog/item.html")

def flowers_catalog(request):
    return render(request, "catalog/flowers_catalog.html")