# Generated by Django 2.1.5 on 2019-02-05 23:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_auto_20190206_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='language',
            field=models.TextField(blank=True, max_length=512, verbose_name='язык'),
        ),
        migrations.AddField(
            model_name='shopuserprofile',
            name='url',
            field=models.TextField(blank=True, max_length=512, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 23, 16, 43, 34083, tzinfo=utc), null=True),
        ),
    ]
