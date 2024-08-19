from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_room, name='create_room'),
    path('join-room/', views.join_room, name='join_room'),
    path('room/<str:room_code>/', views.room, name='room'),
]
