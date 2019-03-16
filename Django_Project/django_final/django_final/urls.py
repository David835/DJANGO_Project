
from django.contrib import admin
from django.urls import path, include
# from django_final.core.views import search
from django_final.core.urls import core_patterns

urlpatterns = [
    path('', include(core_patterns)),
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path
from core.views import search

urlpatterns = [
    path('search/', search, name="buscar"),
    path('admin/', admin.site.urls),
]