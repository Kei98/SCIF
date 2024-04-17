from django.db import IntegrityError
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

@api_view(['GET'])
def user_list(request, format=None):
    users = User.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def user_post(request, format=None):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UsersSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.user_active = 0
        serializer1 = UserSerializer(user)
        request.data['_mutable'] = True
        request.data.update(serializer1.data)
        request.data['_mutable'] = False
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
def user_info_list(request, format=None):
    if request.method == 'GET':
        users_info = UserInfo.objects.all()
        serializer = UserInfoSerializer(users_info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_info_detail(request, id, format=None):
    try:
        user_info = UserInfo.objects.get(pk=id)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserInfoSerializer(user_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            user_info.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except IntegrityError as e:
            user_info.user_info_active = 0
            serializer1 = UserInfoSerializer(user_info)
            request.data['_mutable'] = True
            request.data.update(serializer1.data)
            request.data['_mutable'] = False
            serializer = UserInfoSerializer(user_info, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Will be deactivated because of dependent data", status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(['GET', 'POST'])
def user_role_list(request, format=None):
    if request.method == 'GET':
        user_roles = UserRole.objects.all()
        serializer = UserRoleSerializer(user_roles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)