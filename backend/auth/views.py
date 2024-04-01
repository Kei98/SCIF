from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user.serializers import *

@api_view(['POST'])
def login(request, format=None):

    return Response({})

@api_view(['POST'])
def signup(request, format=None):
    return Response({})


@api_view(['GET'])
def test_token(request, format=None):
    return Response({})



