from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("chat/", views.chat, name="chat"),
    path("my-tickets/", views.my_tickets, name="my_tickets"),
    path("service-status/", views.service_status, name="service_status"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.user_logout, name="logout"),
    path("new-chat/", views.new_chat, name="new_chat"),

]