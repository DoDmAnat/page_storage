from django.db import models


class ContentBlock(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    show_count = models.IntegerField(default=0)

    def increment_show_count(self):
        self.show_count += 1
        self.save()

    class Meta:
        ordering = ['sort_order']

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField()
    content_blocks = models.ManyToManyField(ContentBlock)

    class Meta:
        ordering = ['sort_order']