# Generated by Django 5.0.6 on 2024-05-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
    ]
