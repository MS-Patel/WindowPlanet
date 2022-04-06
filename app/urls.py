from . import views
from django.urls import path


app_name="app"

urlpatterns = [
    path('', views.home, name="home"),
    path('qoute', views.qoute, name="qoute"),
    path('partial/<id>', views.partial, name="partial"),
]

