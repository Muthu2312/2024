from django.urls import path
from Registration import views

urlpatterns = [
    path("",views.Landing.as_view(),name="Landing"),
    path("Register/",views.Register.as_view(),name="Register"),
    path("Login/",views.Login.as_view(),name="Login"),
]