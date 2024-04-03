from django.shortcuts import render

# Create your views here.
from .models import student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=student.object.all()
    serializer_class=StudentSerializers
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]