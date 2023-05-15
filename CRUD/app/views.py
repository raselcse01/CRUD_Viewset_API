from django.shortcuts import render
from app.models import Student

from django.shortcuts import get_object_or_404
from app.serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    # get
    def list(self, request):
        set = Student.objects.all()
        serializer = StudentSerializer(set, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        set = Student.objects.all()
        student = get_object_or_404(set, pk=pk)
        serializer = StudentSerializer()
        return Response(serializer.data)
    
    # post
    def create(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    # update

    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)