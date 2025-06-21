from django.urls import path
from . import views

urlpatterns = [
    path('',views.bill_list, name = 'bill_list'),
    path('add/',views.bill_create, name = 'bill_add' ),
    path('add/<int:room_id>/', views.bill_create_for_room, name='bill_add_for_room'),

]
