from django.urls import path
from . import views
from .views import home_view,room_detail_view

urlpatterns = [
    path('create/',views.room_create ,name="room_create"),
    path('update/<int:pk>',views.room_update ,name="room_update"),
    path('delete/<int:pk>',views.room_delete ,name="room_delete"),
    path('', home_view, name='home'),
    path('room/<int:room_id>/', room_detail_view, name='room_detail'),
]
