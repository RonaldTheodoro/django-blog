from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('title', max_length=120)
    content = models.TextField('content')
    image = models.ImageField('image', null=True, blank=True)
    updated = models.DateTimeField(
        'updated',
        auto_now=True,
        auto_now_add=False
    )
    timestamp = models.DateTimeField(
        'timestamp',
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})
