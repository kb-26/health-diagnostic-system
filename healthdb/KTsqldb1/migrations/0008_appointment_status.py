# Generated by Django 2.1.3 on 2018-11-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KTsqldb1', '0007_auto_20181023_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
