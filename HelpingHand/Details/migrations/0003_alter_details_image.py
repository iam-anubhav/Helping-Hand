# Generated by Django 4.1.2 on 2022-11-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0002_alter_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
