# Generated by Django 5.1.1 on 2025-01-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Your_country',
            field=models.CharField(default='India', max_length=50),
        ),
    ]
