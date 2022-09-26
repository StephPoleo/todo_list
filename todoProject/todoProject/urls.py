from django.contrib import admin
from django.urls import path

from todoApp.views import todoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView),
]
