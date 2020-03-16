from django.test import TestCase
from django.shortcuts import reverse

from ..views import index


class ViewTestCase(TestCase):
    def test_page_not_found(self):
        response = self.client.get('/page_that_does_not_exist')
        self.assertEqual(response.status_code, 404)


class IndexViewTest(TestCase):
    def test_view_exists(self):
        response = self.client.get(reverse(index))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse(index))
        self.assertTemplateUsed(response, 'index.html')