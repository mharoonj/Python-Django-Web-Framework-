from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print("args :", args, kwargs)
    print("request :", request.user)
    # return  HttpResponse("<h1>Hello World</h1>") 
    return render(request, "home.html", {})


def contact_view(request,*args, **kwargs):
    my_context = {
        "my_text":"this is contact us",
        "my_number":32050,
        "my_list":["haroon", "fareed"]
    }
    # return  HttpResponse("<h1>Hello World</h1>") 
    return render(request, "contact.html", my_context)


