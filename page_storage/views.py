from rest_framework import generics
from .models import Page
from .serializers import PageDetailSerializer, PageSerializer


class PageListAPIView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailAPIView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        content_blocks = instance.content_blocks.all()
        for content_block in content_blocks:
            content_block.increment_show_count()
        return self.retrieve(request, *args, **kwargs)
