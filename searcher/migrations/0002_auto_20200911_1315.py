# Generated by Django 3.1.1 on 2020-09-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryparam',
            name='answers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='queryparam',
            name='user',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='queryparam',
            name='views',
            field=models.IntegerField(null=True),
        ),
    ]
