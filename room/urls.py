from django.urls import path
from room import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rooms/<str:room>/', views.room, name="room"),
    path('check', views.check, name="check"),
    path('send', views.send, name="send"),
    path('messages/<str:room>/', views.messages, name="messages"),
]
