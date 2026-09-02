from rest_framework.routers import DefaultRouter
from .views.RegisterView import RegisterView
from .views.LoginView import LoginView
from .views.LogoutView import LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
router = DefaultRouter()

router.register("login", LoginView, basename="login")
router.register("logout", LogoutView, basename="logout")
router.register("register", RegisterView, basename="register")

urlpatterns = [
    path("token/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),
]

