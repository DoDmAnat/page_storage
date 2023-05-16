from rest_framework import serializers
from .models import ContentBlock, Page


class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ('name', 'video_link', 'show_count')


class PageSerializer(serializers.ModelSerializer):
    page_url = serializers.HyperlinkedIdentityField(
        view_name='page-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Page
        fields = ('title', 'page_url',)


class PageDetailSerializer(serializers.ModelSerializer):
    content_blocks = serializers.SerializerMethodField()

    def get_content_blocks(self, page):
        sort_field = page.sort_field
        content_blocks = page.content_blocks.all().order_by(sort_field)
        return ContentBlockSerializer(content_blocks, many=True).data

    class Meta:
        model = Page
        fields = ('title', 'content_blocks',)
