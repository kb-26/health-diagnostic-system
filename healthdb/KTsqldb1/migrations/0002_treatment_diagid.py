# Generated by Django 2.1.1 on 2018-09-26 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KTsqldb1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='diagID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='KTsqldb1.Diagnosis'),
            preserve_default=False,
        ),
    ]
