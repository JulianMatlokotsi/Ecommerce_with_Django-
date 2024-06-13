from django.shortcuts import render

def home(request):
    context={}
    return render(request, "MyEcomApp/home.html", context)

def Products(request):
    Products = Products.objects.all()
    context={}
    return render(request, "MyEcomApp/products.html", context)
