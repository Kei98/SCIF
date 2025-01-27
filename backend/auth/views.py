from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.http import JsonResponse
from django.urls import reverse_lazy
import json

class CustomPasswordResetView(PasswordResetView):
    email_template_name = '../../templates/registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            request.POST = request.POST.copy()
            request.POST['email'] = data.get('email', '')
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        if not request.POST['email']:
            return JsonResponse({"error": {"email": ["This field is required."]}}, status=400)

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('self')
        print(self)
        print('form')
        print(form)
        form.save(
            request=self.request,
            email_template_name=self.email_template_name,
        )
        return JsonResponse({"message": "Password reset email sent successfully"}, status=200)

    def form_invalid(self, form):
        print('self')
        print(self)
        print('form')
        print(form)
        return JsonResponse({"error": form.errors}, status=400)

class CustomPasswordResetDoneView(PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Password reset process completed."}, status=200)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def form_valid(self, form):
        form.save()
        return JsonResponse({"message": "Password reset successfully."}, status=200)

    def form_invalid(self, form):
        return JsonResponse({"errors": form.errors}, status=400)

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "Password reset process is complete."}, status=200)

@api_view(['POST'])
def login(request, format=None):
    user = get_object_or_404(User, email=request.data['email'])
    if not user.check_password(request.data['password']) or not user.user_active:
        return Response({"detail": 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

# @api_view(['POST'])
# def signup(request, format=None):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request, format=None):
    return Response("passed for {}".format(request.user.email))



