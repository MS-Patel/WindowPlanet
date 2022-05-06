from . import views
from django.urls import path


app_name="app"

urlpatterns = [
    path('', views.home, name="home"),
    path('qoute', views.qoute, name="qoute"),
    path('partial/<id>', views.partial, name="partial"),
    path('deletepartial/', views.delpartial, name="deletepartial"),
    path('tab_content',views.tab_content,name="tab_content"),
    
]

