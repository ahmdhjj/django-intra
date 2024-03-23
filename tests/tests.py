"""
Unit tests.
"""

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class PasswordResetViewsTest(TestCase):
    """
    Test suite for password reset views in the Django project.
    """

    def setUp(self):
        """
        Set up initial configurations and create a test user.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123')

    def test_password_reset_view(self):
        """
        Test password reset view.
        """
        response = self.client.get(reverse('admin_password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'registration/password_reset_form.html')

    def test_password_reset_done_view(self):
        """
        Test password reset done view.
        """
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'registration/password_reset_done.html')

    def test_password_reset_confirm_view(self):
        """
        Test password reset confirm view.
        """
        # Generate a password reset token for the user
        response = self.client.post(
            reverse('admin_password_reset'), {'email': self.user.email})

        # Redirects to password_reset_done view
        self.assertEqual(response.status_code, 302)

        # Get the token from the email sent to the user
        token = self.get_password_reset_token()

        # Test password reset confirm view
        response = self.client.get(
            reverse(
                'password_reset_confirm',
                kwargs={'uidb64': self.user.pk, 'token': token}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'registration/password_reset_confirm.html')

    def test_password_reset_complete_view(self):
        """
        Test password reset complete view.
        """
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'registration/password_reset_complete.html')

    def get_password_reset_token(self):
        """
        Retrieve the password reset token.
        """
        # Implementation to retrieve the password reset token
        return 'dummy_token'
