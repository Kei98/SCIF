from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('purchases', purchase_list),
    path('purchases/', purchase_post),
    path('purchases/<int:id>', purchase_detail),
    path('purchasesdet', purchase_det_list),
    path('purchasesdet/', purchase_det_post),
    path('purchasesdet/<int:id>', purchase_det_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)