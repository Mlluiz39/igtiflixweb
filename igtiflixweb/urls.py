
from django.contrib import admin
from django.urls import path, include

from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='inicio/', view=include('inicio.urls')),
    path(route='genero/', view=include('genero.urls'))
]
