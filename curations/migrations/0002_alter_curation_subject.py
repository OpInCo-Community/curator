# Generated by Django 4.0.2 on 2022-02-19 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curations', to='curations.subject'),
        ),
    ]
