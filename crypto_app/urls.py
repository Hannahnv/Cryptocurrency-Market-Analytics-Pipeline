# crypto_app/urls.py - Cấu hình URL cho ứng dụng
from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_view, name='import_view'),  # Route mặc định
]