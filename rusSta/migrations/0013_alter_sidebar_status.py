# Generated by Django 3.2.11 on 2022-01-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rusSta', '0012_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(2, '展示'), (1, '隐藏')], default=2, verbose_name='状态'),
        ),
    ]
