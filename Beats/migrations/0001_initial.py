# Generated by Django 4.1.7 on 2025-06-03 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=10)),
                ('audio', models.FileField(upload_to='beats/audio/')),
                ('coverImage', models.ImageField(blank=True, null=True, upload_to='beats/covers/')),
                ('isPublished', models.BooleanField(default=False)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beats', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Beats',
                'ordering': ['-created_at'],
            },
        ),
    ]
