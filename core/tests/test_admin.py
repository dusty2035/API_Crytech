from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            phone_number="09127478007",
            password='test123654'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            phone_number="09127478006",
            password='test123654',
            first_name="test",
            last_name='test',
            email='example@gmail.com',
            address='address'
        )

    def test_users_listed(self):
        """ Tests users are listed in user pages """
        url = reverse("admin:core_user_changelist")
        # response
        res = self.client.get(url)

        # checks response if it contains clients information

        self.assertContains(res, self.user.phone_number)
        self.assertContains(res, self.user.first_name)

    def test_user_change_page(self):
        """ Tests that the user edit page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that the create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)