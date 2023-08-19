
from django.urls import path
from .views import index

#handles urls
urlpatterns = [

    path('',index)
    
]
