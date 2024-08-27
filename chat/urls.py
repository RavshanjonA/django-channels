from django.urls import path

from chat import views

app_name = "chat"
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('rooms/', views.RoomsView.as_view(), name="rooms"),
    path('room/<slug:slug>/', views.RoomView.as_view(), name="room"),
]
