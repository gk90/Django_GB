# Generated by Django 2.1.5 on 2019-02-05 21:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_auto_20190205_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 21, 5, 45, 998032, tzinfo=utc), null=True),
        ),
    ]
