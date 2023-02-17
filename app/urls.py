from django.urls import path
from . import views
from .views import ShowAPI

urlpatterns = [
    path('',views.show),
    path('api/<pk>',ShowAPI.as_view()),
    
]
