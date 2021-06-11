from django.urls import path
from . views import RegisterView, UserLoginView, ContactList, ContactDetail

urlpatterns = [
  path("register/", RegisterView.as_view()),
  path("login/", UserLoginView.as_view()),
  path("contacts/", ContactList.as_view()),
  path("contacts/<int:id>/", ContactDetail.as_view()),
]