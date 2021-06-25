from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='Pages'),
    # Common
    path('login/', views.LoginClass.as_view(), name='login'),
    path('dashboard/', views.DashboardClass.as_view(), name='dashboard'),
    # User
    path('change-password/', views.ChangePasswordClass.as_view(), name='change_password'),


]
