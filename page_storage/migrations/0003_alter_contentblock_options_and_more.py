# Generated by Django 4.2.1 on 2023-05-16 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_storage', '0002_alter_contentblock_options_alter_page_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentblock',
            options={},
        ),
        migrations.RemoveField(
            model_name='contentblock',
            name='sort_order',
        ),
    ]
