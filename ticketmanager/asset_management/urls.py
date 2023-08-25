from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/add/', views.add_asset, name='add_asset'),
    path('assets/update/<int:asset_id>/', views.update_asset, name='update_asset'),
    path('assets/delete/<int:asset_id>/', views.delete_asset, name='delete_asset'),
    path('home/', views.home, name='home'),
]
