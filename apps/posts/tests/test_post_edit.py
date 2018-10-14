from django.test import TestCase
from django.urls import reverse

from .. import models


class TestPostUpdate(TestCase):

    def setUp(self):
        self.post = models.Post.objects.create(
            title='title',
            content='content'
        )
        self.response = self.client.get(
            reverse('posts:edit', kwargs={'pk': self.post.pk})
        )

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/form.html')
