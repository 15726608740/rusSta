# Generated by Django 3.2.11 on 2022-01-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rusSta', '0013_alter_sidebar_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='name',
            field=models.CharField(default='abc', max_length=61, verbose_name='收藏名称'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '隐藏'), (2, '展示')], default=2, verbose_name='状态'),
        ),
    ]
