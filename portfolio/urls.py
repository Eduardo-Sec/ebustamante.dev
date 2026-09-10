from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playbook/', include('playbook.urls')),
    path('', include('core.urls')),
]
