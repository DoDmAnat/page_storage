# Generated by Django 4.2.1 on 2023-05-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_storage', '0003_alter_contentblock_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentblock',
            options={'ordering': ['name', 'video_link', 'show_count']},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['sort_field']},
        ),
        migrations.RemoveField(
            model_name='page',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='page',
            name='sort_field',
            field=models.CharField(choices=[('name', 'Name'), ('video_link', 'Video Link'), ('show_count', 'Show Count')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
