# Generated by Django 3.2 on 2022-04-08 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20220408_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='influencerfaq',
            old_name='influencer_username',
            new_name='influencer_username2',
        ),
        migrations.RenameField(
            model_name='influencerpackage',
            old_name='influencer_username',
            new_name='influencer_username1',
        ),
    ]
