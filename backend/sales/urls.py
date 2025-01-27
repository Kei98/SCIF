from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('inventoryreport', inventoryView),
    path('purchasesvssales/', CreateSalesView.as_view({'get': 'list'})),
    path('inventoryreport/', CreateInventoryView.as_view({'get': 'list'})),
    path('paymentmethods', payment_method_get),
    # path('paymentmethods/<int:id>', quote_detail),
    # path('salesstatus', quote_list),
    # path('salesstatus/<int:id>', quote_detail),
    path('sales', sales_get),
    path('sales-or', sales_get_or),
    path('sales/', CreateSaleView.as_view(), name='create-sale'),
    path('sales-list/', SalesListView.as_view(), name='sales-list'),
    path('sales/<int:sales_id>/', SalesListView.as_view(), name='sales-delete'),
    path('sales/<int:sales_id>/details/', SalesDetailsView.as_view(), name='sales-details'),
    path('sales-details/<int:detail_id>/', SalesDetailUpdateView.as_view(), name='sales-detail-update'),
    # path('sales/<int:id>', quote_answer_detail),
    # path('salesdets', quote_answer_list),
    # path('salesdets/', quote_answer_post),
    # path('salesdets/<int:id>', quote_answer_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)