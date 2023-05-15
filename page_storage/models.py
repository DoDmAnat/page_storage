from django.db import models

class Ip(models.Model):
    ip = models.CharField(max_length=100)

def __str__(self):
    return self.ip

class ContentBlock(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    show_count = models.IntegerField(default=0)

    def increment_show_count(self):
        self.show_count += 1
        self.save()

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField()
    content_blocks = models.ManyToManyField(ContentBlock)