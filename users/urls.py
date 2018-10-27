from django.urls import path

from . import views
app_name = 'users'
urlpatterns = [
    path("/login", views.LoginFormView.as_view(), name="login" ),
    path("/logout", views.LogoutView.as_view(), name="logout" ),
    path("/register", views.register, name="register" ),
]