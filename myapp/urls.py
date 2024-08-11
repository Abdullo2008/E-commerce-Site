from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>/', category, name='category'),
    path('product/<int:id>/add/', add_view, name='add'),
    path('product/<int:id>/', sell_view, name='sell'),
    # Product CRUD
    path('add_product/', AddProduct.as_view(), name='add_product'),
    path('retrieve_product/', RetrieveProduct, name='retrieve_product'),
    path('update_product/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    # Category CRUD
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('retrieve_category/', RetrieveCategory, name='retrieve_category'),
    path('update_category/<int:pk>/', UpdateCategory.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', DeleteCategory.as_view(), name='delete_category'),
]
