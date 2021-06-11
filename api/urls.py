from django.urls import path
from . views import RegisterView, UserLoginView

urlpatterns = [
  path("register/", RegisterView.as_view()),
  path("login/", UserLoginView.as_view()),
]