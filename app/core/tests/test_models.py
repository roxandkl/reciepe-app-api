from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@gmail.com', password = 'testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)



class ModelTests(TestCase):
    
    def test_create_user_with_email_successfull(self):
        """ Test success of creating new user with email."""

        email = 'test@gmail.com'
        password = 'Test12345'
        user = get_user_model().objects.create_user(
            email= email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Normalize user given email."""

        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test12345')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """User created with no email raises Error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')


    def test_create_superuser(self):
        """Test creating a new superuser"""
        
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        

    def test_tag_str(self):
        """Test tag string representation"""
        tag=models.Tag.objects.create(
            user=sample_user(),
            name = vegan
        )

        self.assertEqual(str(tag), tag.name)


    
    
