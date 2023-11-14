from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users', user_list),
    path('users/', user_post),
    path('users/<int:id>', user_detail),
    path('usersinfo/', user_info_list),
    path('usersinfo/<int:id>', user_info_detail),
    path('usersrole/', user_role_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)