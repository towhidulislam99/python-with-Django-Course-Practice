# Generated by Django 4.2.5 on 2023-10-12 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_demo_user_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo_user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]