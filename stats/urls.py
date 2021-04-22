from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comunas', views.get_communes_info, name='get_communes_info'),
]