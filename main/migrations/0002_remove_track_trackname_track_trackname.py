# Generated by Django 4.1.6 on 2023-02-09 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='trackname',
        ),
        migrations.AddField(
            model_name='track',
            name='trackname',
            field=models.CharField(default=1, max_length=264, unique=True),
            preserve_default=False,
        ),
    ]
