# Generated by Django 3.2.11 on 2022-01-27 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rusSta', '0016_remove_collection_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='aaaaa')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='ssss')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rusSta.userinfo', verbose_name='收藏人')),
                ('title', models.ForeignKey(max_length=61, on_delete=django.db.models.deletion.CASCADE, to='rusSta.post', verbose_name='收藏文章')),
            ],
            options={
                'verbose_name': 'ceshi',
                'verbose_name_plural': 'ceshi',
            },
        ),
    ]
