from django.test import TestCase

class TunesViewTestCase(TestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view_get(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        response = self.client.post('/login/', {
            'username': 'username',
            'password': 'password'
        }, follow=True)
        self.assertRedirects(response, '/')

