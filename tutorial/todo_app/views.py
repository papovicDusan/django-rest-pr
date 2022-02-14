import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from todo_app.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class UsersView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        return User.objects.filter(Q(first_name__contains = name) | Q(last_name__contains = name))

class UserAuthView(APIView):
    def get(self,request):
        if self.request.user.is_authenticated:
            serializer = UserSerializer(self.request.user)
            return Response(serializer.data)
        else:
            raise ValidationError("You are not authenticated!")
        
class UserSetView(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
# Create your views here.
class HomeView(APIView):
    pass