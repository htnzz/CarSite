# Generated by Django 5.1.3 on 2024-12-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_customer_photo_review_photo_review_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(null=True, upload_to='uploads/photo/', verbose_name='Фото'),
        ),
    ]
