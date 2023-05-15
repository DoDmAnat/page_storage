from django.contrib import admin

from .models import ContentBlock, Ip, Page

admin.site.register(ContentBlock)
admin.site.register(Ip)
admin.site.register(Page)
