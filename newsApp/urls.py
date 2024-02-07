from django.contrib import admin
from django.urls import path,include
from news_api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news_api.urls')),
]
