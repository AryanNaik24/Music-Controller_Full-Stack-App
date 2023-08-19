

from django.urls import path 
from .views import RoomView

urlpatterns = [
    #calls main function if we dont have url
    path('room',RoomView.as_view())
]
