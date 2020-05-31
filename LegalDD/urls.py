"""LegalDD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_view),
    path('upload/', UploadDocument.as_view()),
    path('documents/<str:name>/', document_view),
    path('admin_urls/', login_required(admin_view)),
    path('edit/<str:name>/', edit_view),
    path('download/<str:name>/', download_view),
]
