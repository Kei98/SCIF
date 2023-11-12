"""
URL configuration for SCIF_home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import *
from product import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', user_list),
    path('users/', user_post),
    path('users/<int:id>', user_detail),
    path('usersinfo/', user_info_list),
    path('usersinfo/<int:id>', user_info_detail),
    path('usersrole/', user_role_list),
    
    path('products', views.product_list),
    path('products/', views.product_post),
    path('products/<int:id>', views.product_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
