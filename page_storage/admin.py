from django import forms
from django.contrib import admin

from .models import ContentBlock, Page

class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

    sort_order = forms.ChoiceField(choices=[('name', 'Name'), ('show_count', 'Show Count')])

class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm

admin.site.register(ContentBlock)
admin.site.register(Page, PageAdmin)
