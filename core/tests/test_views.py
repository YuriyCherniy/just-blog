from django.test import TestCase, Client


class CoreViewsTesCase(TestCase):
    def setUp(self):
        self.c = Client()

    # status code 200
    def test_index_view_status_code_200(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    # template used
    def test_index_view_template_used(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'core/index.html')
