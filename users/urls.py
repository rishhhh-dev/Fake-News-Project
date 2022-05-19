from django.urls import path
from users import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(
        template_name='users/templates/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(
        template_name='users/templates/logout.html'),name='logout'),
]