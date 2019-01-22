# Generated by Django 2.1.5 on 2019-01-22 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190122_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adv_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='adv_info', to='core.UserAdvInfo'),
        ),
    ]
