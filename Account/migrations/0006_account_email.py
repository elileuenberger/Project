# Generated by Django 2.1.7 on 2019-03-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_account_currentuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]