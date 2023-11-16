from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('suppliersinfo/', supplier_list),
    path('supplierinfo/<int:id>', supplier_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)