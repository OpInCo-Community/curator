# Generated by Django 4.0.2 on 2022-02-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userProfiles", "0002_auto_20211222_1839"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(
                blank=True,
                default="/static/images/default_profile.jpg",
                null=True,
                upload_to="profile_pic/",
            ),
        ),
    ]
