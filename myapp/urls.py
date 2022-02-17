from unicodedata import name
import django


from django.urls import path 
from . import views as v

urlpatterns = [ 
    path('', v.user_login, name='login'),
    path('signup/', v.user_create, name='signup'),
    path('product_create/', v.product_create, name='product_create'),
    path('get_products/', v.get_products, name='get_products'),
    path('delete_product/<int:id>/', v.delete_product, name='delete_product'),
    path('product_update/<int:id>/', v.product_update, name='product_update'),
]