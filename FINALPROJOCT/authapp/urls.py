from django.urls import path
from .views import HomePage, Register, Login,  logoutuser,Profile,admin_dashboard_view

urlpatterns = [
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('profile/', Profile, name='profile'),

    path('admin-dashboard',admin_dashboard_view,name='admin-dashboard'),

]