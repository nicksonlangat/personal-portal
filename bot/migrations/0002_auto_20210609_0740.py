# Generated by Django 3.2.3 on 2021-06-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
