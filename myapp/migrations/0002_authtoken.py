# Generated by Django 3.2.7 on 2024-08-01 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
            ],
            options={
                'verbose_name': 'Auth User Token',
                'verbose_name_plural': 'Auth Token',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('authtoken.token',),
        ),
    ]
