# Generated by Django 2.1.7 on 2019-04-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab', '0004_auto_20190402_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='endTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lab',
            name='sectionNumber',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='lab',
            name='startTime',
            field=models.IntegerField(default=0),
        ),
    ]
