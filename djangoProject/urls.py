"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from one_day.views import show_number
from django_1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/<int:number>', show_number),
    path('hello/', views.show_hello),
    path('random/', views.show_random),
    # path('randomnum/<int:max_number>', views.pick_number),
    re_path(r'^randomnum/(?P<max_number>(\d)+)/$', views.pick_number),
]
