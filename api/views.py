from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from . serializers import UserSerializer, ContactSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import Contact
from rest_framework import permissions
# Create your views here.
#Crud views
class ContactList(ListCreateAPIView):
  serializer_class = ContactSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  def get_queryset(self):
    return Contact.objects.filter(owner=self.request.user)

class ContactDetail(RetrieveUpdateDestroyAPIView):
  serializer_class = ContactSerializer
  permission_classes = (permissions.IsAuthenticated,)

  lookup_field = "id"
 
  def get_queryset(self):
    return Contact.objects.filter(owner=self.request.user)


#Authentication Vies
class RegisterView(GenericAPIView):
  serializer_class = UserSerializer

  def post(self, request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(GenericAPIView):
  serializer_class = LoginSerializer
  def post(self, request):
    data = request.data
    username = data.get('username', '')
    password = data.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user:
      auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)

      serializer = UserSerializer(user)

      data = {
        "user": serializer.data,
        "token": auth_token
      }

      return Response(data, status=status.HTTP_200_OK)
      #SEND Res

    return Response({
      'detail': "Invalid Credetials"
    }, status=status.HTTP_401_UNAUTHORIZED)

    