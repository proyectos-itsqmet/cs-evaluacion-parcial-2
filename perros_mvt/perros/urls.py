from django.urls import path
from .views import *

urlpatterns = [
    path("", perro_list, name = "perro_list"),
    path("perro/<int:id>", perro_detail, name = "perro_detail"),
    path("perro/create", perro_create, name = "perro_create"),
    path("perro/update/<int:id>", perro_update, name = "perro_update"),
    path("perro/delete/<int:id>", perro_delete, name = "perro_delete"),
]
