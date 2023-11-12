
from django.urls import path
from . import views


urlpatterns = [
     path('', views.welcome, name='welcome'),
        path('my-view/', views.my_view, name='my_view'),
         path('success/', views.success_page, name='success_page'),
]