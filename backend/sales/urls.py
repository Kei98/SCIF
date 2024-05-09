from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('inventoryreport', inventoryView),
    path('salesreport', sales_report),
    path('inventoryreport/', CreateInventoryView.as_view({'get': 'list'})),
    # path('paymentmethods/<int:id>', quote_detail),
    # path('salesstatus', quote_list),
    # path('salesstatus/<int:id>', quote_detail),
    # path('sales', quote_answer_list),
    # path('sales/', quote_answer_post),
    # path('sales/<int:id>', quote_answer_detail),
    # path('salesdets', quote_answer_list),
    # path('salesdets/', quote_answer_post),
    # path('salesdets/<int:id>', quote_answer_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)