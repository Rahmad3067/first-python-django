from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    # we can add <str:pk> as string primary key so we can access it dinamicly in views and we pass pk there
    path('room/<str:pk>/', views.room, name="room"),
]
