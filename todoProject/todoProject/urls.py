from django.contrib import admin
from django.urls import path, include

#from todoApp.views import todoView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('todo/', todoView),
    path('', include('todoApp.urls'))
]
