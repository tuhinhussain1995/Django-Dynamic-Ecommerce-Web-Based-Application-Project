# Generated by Django 3.0.2 on 2020-06-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablebloodgroup',
            name='apply_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]