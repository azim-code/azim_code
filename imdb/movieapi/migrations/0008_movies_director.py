# Generated by Django 3.1.1 on 2020-09-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0007_auto_20200911_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
