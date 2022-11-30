from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index" ),
    path("vaccancies", views.vaccancies, name="vaccancies" ),
    path("login", views.login_view, name="login" ),
    path("jobs", views.jobs, name="jobs" ),
    path("user", views.user, name="user" ),
    path("register", views.register, name="register" ),
    path("aboutus", views.aboutus, name="aboutus" ),
    path("logout", views.logout_view, name="logout" )
]
