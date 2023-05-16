from django.db import models


class ContentBlock(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)
    show_count = models.IntegerField(default=0)

    def increment_show_count(self):
        self.show_count += 1
        self.save()

    class Meta:
        ordering = ['name', 'video_link', 'show_count']

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_field = models.CharField(max_length=255, choices=(
        ('name', 'Name'),
        ('video_link', 'Video Link'),
        ('show_count', 'Show Count'),
    ))
    content_blocks = models.ManyToManyField(ContentBlock)

    def __str__(self):
        return self.title
