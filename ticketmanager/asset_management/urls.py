from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/add/', views.add_asset, name='add_asset'),
    path('assets/<int:asset_id>/update/', views.update_asset, name='update_asset'),
    path('assets/<int:asset_id>/delete/', views.delete_asset, name='delete_asset'),
    path('home/', views.home, name='home'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
