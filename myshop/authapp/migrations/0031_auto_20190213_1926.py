# Generated by Django 2.1.5 on 2019-02-13 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0030_auto_20190213_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 26, 57, 784377, tzinfo=utc), null=True),
        ),
    ]
