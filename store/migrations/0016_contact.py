# Generated by Django 3.1.1 on 2020-09-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20200921_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
    ]
