"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from user.serializers import UserRoleSerializer, UserInfoSerializer
from user.models import UserInfo, UserRole

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


class ModelTests(TestCase):
    """Test models"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        serializerInfo = UserInfoSerializer(user_info)
        id = serializerInfo.data['user_info_id']
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'

        role_id = serializer.data['user_role_id']
        password = 'testpass123'
        # user = get_user_model().objects.create_user(
        #     email=email,
        #     id=user_info,
        #     role= role_id,
        #     password=password,
        # )

        # self.assertEqual(user.user_email, email)
        # self.assertTrue(user.check_password(password))
        payload = {
            'id': id,
            'email': email,
            'role': role,
            'password': password,
        }
        res = self.client.post(CREATE_USER_URL, payload)
        print('CREATE_USER_URL')
        print(res.request.__str__())

        print('CREATE_USER_URL')
        print(res.content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists"""
        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'
        role_id = serializer.data['user_role_id']
        password = 'testpass123'
        payload = {
            'email': email,
            'id': user_info,
            'role': role,
            'password': password,
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password is less than 8 chars"""
        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'
        role_id = serializer.data['user_role_id']
        password = 'pw'
        payload = {
            'email': email,
            'id': user_info,
            'role': role,
            'password': password,
        }
        # create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test generates token for valid credentials"""

        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'
        role_id = serializer.data['user_role_id']
        password = 'testpass123'
        user_details = {
            'email': email,
            'id': user_info,
            'role': role,
            'password': password,
        }
        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': user_details['password']
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentials(self):
        """Test returns error if credentials invalid"""

        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'
        role_id = serializer.data['user_role_id']
        password = 'testpass123'
        user_details = {
            'email': email,
            'id': user_info,
            'role': role,
            'password': password,
        }
        create_user(**user_details)

        payload = {
            'email': 'em',
            'password': 'mypass'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test posting a blank password returns an error"""
        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'
        role_id = serializer.data['user_role_id']
        password = 'testpass123'
        user_details = {
            'email': email,
            'id': user_info,
            'role': role,
            'password': password,
        }
        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': ''
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test authentication is required for users"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        user_info = UserInfo.objects.create(user_info_name='HOLA PRUEBA',
                                            user_info_id_card='u443',
                                            user_info_tel_number='345',
                                            user_info_email='byiuiowe@',
                                            user_info_address='naos'
                                            )
        user_info.save()
        role = UserRole.objects.create(user_role_name='Admin')
        role.save()
        serializer = UserRoleSerializer(role)
        email = 'test@example.com'
        role_id = serializer.data['user_role_id']
        password = 'testpass123'
        self.user = create_user(
            id = user_info,
            email = email,
            password = password,
            user_active = True,
            role = role
        )

        self.client = APIClient()
        self.client.force_authenticate(user = self.user)

    def test_retrieve_profile_success(self):
        """Test retieving profile for logged in user"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'email': self.user.email
        })

    def test_post_me_not_allowed(self):
        """Test POST is not allowed for the me endpoint"""
        res = self.client.post(ME_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating the user profile for the authenticated user"""
        payload = {'email': 'updatedemail@email.com', 'password': 'newPassw21'}

        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.email, payload['email'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)