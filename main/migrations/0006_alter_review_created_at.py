# Generated by Django 5.1.3 on 2024-12-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_review_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]
