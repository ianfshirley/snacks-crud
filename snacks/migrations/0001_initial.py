# Generated by Django 4.1.5 on 2023-01-26 06:07

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
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.URLField(default='https://http.cat/404')),
                ('reference_url', models.URLField(default='https://http.cat/404')),
                ('description', models.TextField(default='')),
                ('purchaser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
