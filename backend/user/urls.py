from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'user'

urlpatterns = [
    path('users', user_list),
    # path('users/', user_post),
    path('users/<int:id>', user_detail),
    path('usersinfo/', user_info_list),
    path('usersinfo/<int:id>', user_info_detail),
    path('usersrole/', user_role_list),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('me/', ManageUserView.as_view(), name = 'me'),
    path('csrf-test/', csrf_test, name='csrf_test'),

]

urlpatterns = format_suffix_patterns(urlpatterns)