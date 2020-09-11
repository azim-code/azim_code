# Generated by Django 3.1.1 on 2020-09-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0005_auto_20200911_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='genre',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(to='movieapi.Genre'),
        ),
    ]