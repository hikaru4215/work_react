from django.urls import path
from api import views



urlpatterns = [
    path('api/',views.ListView.as_view(), name='list'),
    path('api/<int:pk>/',views.DetailView.as_view(), name='detail'),
]