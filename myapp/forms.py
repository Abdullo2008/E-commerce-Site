from django import forms
from .models import Category, ProductModel

class SellForm(forms.Form):
    product_name = forms.CharField()
    amount_taken = forms.IntegerField(min_value=1)


class AddForm(forms.Form):
    product_name = forms.CharField()
    amount_added = forms.IntegerField(min_value=1)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
