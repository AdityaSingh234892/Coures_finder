# Generated by Django 5.1.1 on 2025-01-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_user_your_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gpa_score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gre_score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='toefl_score',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
