# Generated by Django 4.0.2 on 2022-02-19 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curations', to=settings.AUTH_USER_MODEL),
        ),
    ]
