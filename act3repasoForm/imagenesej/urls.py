from django.urls import path
from . import views
urlpatterns = [
    path('', views.bienvenido, name='bienvenido'),
    path('subir/', views.image_upload, name='image_upload'),
     path('galeria/', views.image_gallery, name='image_gallery'),
      path('delete/', views.delete_image, name='delete_image'),
]
