# Generated by Django 3.1.4 on 2021-03-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelFeature', '0002_auto_20200511_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livestream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]