from django.urls import path
from App import views
urlpatterns = [
    path("",views.Login.as_view(),name="Login")
]