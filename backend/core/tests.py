from . models import Contact
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class ContactTestCase(APITestCase):
    """
    Test suite for Contact model
    """

    def setUp(self):
        self.client = APIClient()
        self.data = {
            'name': 'Ben Carson',
            'message': "I'm a big fan of your work",
            'email': 'ben@carson.com'
        }
        self.url = '/contact/'
    
    def test_create_contact(self):
        """
        test ContactViewSet create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().title, 'Ben Carson')
    
    def test_create_contact_without_name(self):
        '''
        test ContactViewSet create method when name is not in data
        '''
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_name_equals_blank(self):
        """
        test ContactViewSet create method when name is blank
        """
        data = self.data
        data['name'] = ''
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_without_message(self):
        """
        test ContactViewSet create method when message is blank
        """
        data = self.data
        data.pop('message')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_message_equals_blank(self):
        """
        test ContactViewSet create method when message is blank
        """
        data = self.data
        data['message'] = ''
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_without_email(self):
        """
        test ContactViewSet create method when email is blank
        """
        data = self.data
        data.pop('email')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_when_email_equals_blank(self):
        """
        test ContactViewSet create method when email is blank
        """
        data = self.data
        data['email'] = ''
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contact_with_invalid_email(self):
        """
        test ContactViewSet create method with invalid email
        """
        data = self.data
        data['email'] = 'test'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)