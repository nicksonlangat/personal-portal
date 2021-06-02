# Generated by Django 3.2.3 on 2021-06-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='PROJECTS')),
                ('live_link', models.CharField(max_length=100)),
                ('code_link', models.CharField(max_length=100)),
            ],
        ),
    ]
