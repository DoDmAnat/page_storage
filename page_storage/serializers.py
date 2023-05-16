from rest_framework import serializers
from .models import ContentBlock, Page

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    page_url = serializers.HyperlinkedIdentityField(
        view_name='page-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Page
        fields = ('title','page_url',)

class PageDetailSerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(many=True)
    
    class Meta:
        model = Page
        fields = ('title','content_blocks',)