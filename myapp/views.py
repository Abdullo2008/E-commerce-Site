from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import SellForm, AddForm, ProductForm, CategoryForm
from .models import ProductModel, Category


def index(request):
    products = ProductModel.objects.all()
    categorys = Category.objects.all()
    context = {
        'products': products,
        'categorys': categorys
    }
    return render(request, 'index.html', context)


def category(request, id):
    products = ProductModel.objects.filter(category_id=id)
    context = {
        'products': products
    }
    return render(request, 'single.html', context)


def sell_view(request, id):
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            amount_taken = form.cleaned_data['amount_taken']

            product = get_object_or_404(ProductModel, name=product_name)

            if product.quantity >= amount_taken:
                product.quantity -= amount_taken
                product.save()
                messages.success(request, f'Успешно продано {amount_taken} единиц товара {product_name}.')
                return redirect('index')
            else:
                messages.error(request, 'Недостаточно доступного количества.')
                return redirect('sell', id=id)  # Redirect to prevent form resubmission
        else:
            messages.error(request, 'Форма недействительна.')
            return redirect('sell', id=id)  # Redirect to prevent form resubmission

    product = get_object_or_404(ProductModel, id=id)
    context = {
        'product': product
    }
    return render(request, 'single_product.html', context)


def add_view(request, id):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            amount_added = form.cleaned_data['amount_added']

            product = get_object_or_404(ProductModel, name=product_name)

            product.quantity += amount_added  # Add the amount to the quantity
            product.save()

            messages.success(request, f'Успешно добавлено {amount_added} единиц товара {product_name}.')
            return redirect('index')
        else:
            messages.error(request, 'Форма недействительна.')
            return redirect('add', id=id)  # Redirect to prevent form resubmission

    product = get_object_or_404(ProductModel, id=id)
    context = {
        'product': product
    }
    return render(request, 'add_quantity_product.html', context)


class AddProduct(CreateView):
    model = ProductModel
    template_name = 'product/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('retrieve_product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context

def RetrieveProduct(request):
    products = ProductModel.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/retrieve_product.html', context)


class UpdateProduct(UpdateView):
    model = ProductModel
    template_name = 'product/update_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('retrieve_product')


class DeleteProduct(DeleteView):
    model = ProductModel
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('retrieve_product')


class AddCategory(CreateView):
    model = Category
    template_name = 'category/add_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy("retrieve_category")


def RetrieveCategory(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys
    }
    return render(request, 'category/retrieve_category.html', context)


class UpdateCategory(UpdateView):
    model = Category
    template_name = 'category/update_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('retrieve_category')


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'category/delete_category.html'
    success_url = reverse_lazy('retrieve_category')
