# Generated by Django 3.1.1 on 2020-09-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0003_auto_20200910_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='user',
        ),
    ]
