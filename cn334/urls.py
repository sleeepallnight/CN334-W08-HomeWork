"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<str:username>/', main_views.user_detail),
    path('product/all/', main_views.product_all),
    path('product/byid/<int:id>/', main_views.productById),
    path('order/byProductId/<int:id>/', main_views.order_by_product_id),
    path('summarize/', main_views.summarize),
]