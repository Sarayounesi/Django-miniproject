# Generated by Django 4.1.2 on 2022-10-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بروزرسانی')),
            ],
        ),
    ]
