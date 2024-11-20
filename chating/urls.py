from django.urls import path
from . import views
# from config.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]