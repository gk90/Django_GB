# Generated by Django 2.1.5 on 2019-02-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество на складе'),
        ),
    ]
