# Generated by Django 3.1.4 on 2021-03-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalOrder', '0004_auto_20201230_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genordertable',
            name='status',
            field=models.TextField(default='Pending Approval'),
        ),
    ]