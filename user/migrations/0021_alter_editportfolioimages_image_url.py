# Generated by Django 3.2 on 2022-04-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_editportfolioimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editportfolioimages',
            name='image_url',
            field=models.ImageField(blank=True, default='', max_length=300, null=True, upload_to=''),
        ),
    ]
