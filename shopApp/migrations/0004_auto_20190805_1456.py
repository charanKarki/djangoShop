# Generated by Django 2.2.3 on 2019-08-05 09:26

from django.db import migrations, models
import shopApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0003_auto_20190805_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopingitem',
            name='itemImg',
            field=models.ImageField(upload_to=shopApp.models.create_filename),
        ),
    ]
