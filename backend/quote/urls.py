from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('quotes', quote_list),
    path('quotes/', quote_post),
    path('quotes/<int:id>', quote_detail),
    path('quoteanswers', quote_answer_list),
    path('quoteanswers/', quote_answer_post),
    path('quoteanswers/<int:id>', quote_answer_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)