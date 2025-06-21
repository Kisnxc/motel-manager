from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenant_list, name='tenant_list'),
    path('create/', views.tenant_create, name='tenant_create'),
    path('create/<int:room_id>/', views.tenant_create_for_room, name='tenant_create_for_room'),

]
