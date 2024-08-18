# downloader/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_download_links, name='get_download_links')
]
