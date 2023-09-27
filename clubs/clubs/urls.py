
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',home),
    path('about/',about),
    path('777/',u_20),
    path('england/',england),
    path('country/',country)
]
