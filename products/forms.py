from django import forms

from .models import Product

class ProductForm(forms.ModelForm ):
    class Meta:
        model= Product
        fields = [
            "title",
            "description",
            "price"
        ]

class RawProductionForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Enter title"})) # with no label on the left
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "rows":10
    }))  # widget to change textfield to textarea
    price = forms.DecimalField(initial=199.99) 