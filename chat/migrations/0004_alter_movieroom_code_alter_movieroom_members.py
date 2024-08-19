# Generated by Django 5.1 on 2024-08-19 10:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_delete_movie_remove_movieroom_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieroom',
            name='code',
            field=models.CharField(default='BD5BAC', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='movieroom',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]