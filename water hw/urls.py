from django.contrib import admin
from django.urls import path
from Clients.views import contacts, info, clients_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('info/', info),
    path('clients/', clients_list)
]