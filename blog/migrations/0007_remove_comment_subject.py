# Generated by Django 3.2.20 on 2023-07-20 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_text_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
