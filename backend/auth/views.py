from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user.serializers import *

@api_view(['POST'])
def login(request, format=None):

    return Response({})

@api_view(['POST'])
def signup(request, format=None):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def test_token(request, format=None):
    return Response({})



