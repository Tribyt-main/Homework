"""
URL configuration for module18 project.

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

from task2.views import func_templates, class_temp, main_page

from task3.views import main_page_task3, shop_page, basket_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_page),
    # path('functemp/', func_templates),
    # path('classtemp/', class_temp.as_view()),  #.as_view для запуска классового метода
    path('', main_page_task3),
    path('shop/', shop_page),
    path('basket/', basket_page),
]
