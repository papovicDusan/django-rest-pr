from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from todo_app.serializers import UserSerializer
from django.contrib.auth.models import User

class UserSetView(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
# Create your views here.
class HomeView(APIView):
    pass