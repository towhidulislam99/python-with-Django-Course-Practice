# Generated by Django 4.2.5 on 2023-10-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bttcadmissionform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_data',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
