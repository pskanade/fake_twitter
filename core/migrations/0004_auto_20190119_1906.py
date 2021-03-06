# Generated by Django 2.1.5 on 2019-01-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190119_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tweet',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=60, unique=True),
        ),
    ]
