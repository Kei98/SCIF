from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('services', service_list),
    path('services/<int:id>', service_detail),
    path('servicesdet', service_det_list),
    path('servicesdet/', service_det_post),
    path('servicesdet/<int:id>', service_det_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)