from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('dashboard/', get_index_page, name='dashboard'),
    path('delete-delete_service/', delete_service, name='delete_service'),
    path('change_service/', change_service, name='change_bank'),
    path('get_service_detail/', get_service_detail, name='get_service_detail'),
    path('add-service/', add_service, name='add_service'),
]
