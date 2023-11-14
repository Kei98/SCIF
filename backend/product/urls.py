from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('products', product_list),
    path('products/', product_post),
    path('products/<int:id>', product_detail),
    path('productsinfo/', product_info_list),
    path('productsinfo/<int:id>', product_info_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)