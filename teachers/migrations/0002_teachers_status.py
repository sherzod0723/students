# Generated by Django 4.2.5 on 2023-10-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
