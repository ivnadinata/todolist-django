from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'webapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('about/', include("about.urls")),
    path('notes/', include("notes.urls")),
]
