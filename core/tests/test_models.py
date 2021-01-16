from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_phone_number(self):
        """ Test creating a new user with phone_number is successfull """
        phone_number = '09127478007'
        email = 'test@gmail.com'
        first_name = 'test'
        last_name = 'test'
        address = 'test address'
        password = 'test123654'
        user = get_user_model().objects.create_user(
            phone_number=phone_number,
            email=email,
            first_name=first_name,
            last_name=last_name, 
            address=address,
            password=password,
        )

        self.assertEqual(user.phone_number, phone_number)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_phone_number(self):
        """ Test creating a new user with no phone number raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123654')

    def test_create_new_superuser(self):
        """ Test creating superuser """
        user = get_user_model().objects.create_superuser(
            '09127478007',
            'test123654'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)