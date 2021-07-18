# Django
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include(("users.urls", "users"), namespace="users"))

]