# Generated by Django 3.0.6 on 2020-05-17 00:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.TimeField(default=datetime.datetime(2020, 5, 17, 0, 51, 33, 382848, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(default=datetime.datetime.now)),
                ('end_time', models.TimeField(default=datetime.datetime.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='app.member')),
            ],
        ),
    ]