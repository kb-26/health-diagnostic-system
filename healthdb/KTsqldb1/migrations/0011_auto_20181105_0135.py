# Generated by Django 2.1.3 on 2018-11-04 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KTsqldb1', '0010_auto_20181104_2218'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('AppDate', 'Time', 'docID')},
        ),
    ]
