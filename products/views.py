from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductionForm
# Create your views here.

def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    
    # ONE WAY
    # context = {
    #     "title" : obj.title,
    #     "description": obj.description
    # }


    # SECOND WAY
    context = {
        "object":obj
    }
    return render(request, 'products/product_detail.html',context)





# def product_create_view(request, *args, **kwargs):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         "form":form
#     }
#     return render(request, 'products/product_create.html',context)



def product_create_view(request, *args, **kwargs):

    my_form = RawProductionForm()
    if request.method == 'POST':
        my_form = RawProductionForm(request.POST)
        if my_form.is_valid():
            print("cleaned data : ",my_form.cleaned_data)
            print("unpacked : ", my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)

    context = {
        "form" : my_form
    }
    return render(request, 'products/product_create.html',context)
