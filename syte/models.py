from django.db import models
from autoslug import AutoSlugField


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text  = models.TextField()

    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True, null=True)

    slug = AutoSlugField(populate_from='title')
    tags = models.ManyToManyField(Tag, related_name="posts")

    class Meta:
        ordering = ["-publish_date"]