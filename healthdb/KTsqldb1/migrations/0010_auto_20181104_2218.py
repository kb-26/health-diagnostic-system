# Generated by Django 2.1.3 on 2018-11-04 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KTsqldb1', '0009_auto_20181104_2206'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('AppointmentID', 'patID', 'docID'), ('AppDate', 'Time', 'docID')},
        ),
    ]