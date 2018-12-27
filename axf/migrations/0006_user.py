# Generated by Django 2.0.6 on 2018-11-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('tel', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=30)),
                ('icon', models.ImageField(upload_to='icons/%Y/%m/%d')),
            ],
        ),
    ]