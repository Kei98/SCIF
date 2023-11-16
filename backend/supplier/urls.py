from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('suppliers', supplier_list),
    path('suppliers/<int:id>', supplier_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)