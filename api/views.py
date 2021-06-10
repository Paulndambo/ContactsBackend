from django.shortcuts import render
from rest_framework.generic import GenericAPIView
# Create your views here.
class RegisterView(GenericAPIView):
  def post(self, request):
    pass