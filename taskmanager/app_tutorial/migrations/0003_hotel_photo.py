# Generated by Django 4.0.3 on 2022-04-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tutorial', '0002_hotel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]