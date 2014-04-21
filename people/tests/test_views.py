from django.test import TestCase

class PeopleTestCase(TestCase):

    def test_jmadLoginView(self):
        """
        Since we're overriding the LoginView, we've 
        at least got to make sure it returns a 200
        """
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
