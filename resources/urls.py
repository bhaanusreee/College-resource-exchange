from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('upload/', views.resource_upload, name='resource_upload'),
    path('resource/<int:pk>/request/', views.resource_request, name='resource_request'),
    path('request-board/', views.request_board, name='request_board'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('sell/', views.sell_resources, name='sell_resources'),
    path('resource/<int:pk>/delete/', views.resource_delete, name='resource_delete'),
] 