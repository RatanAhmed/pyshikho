# Generated by Django 4.2.5 on 2023-10-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_learncodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='learncodes',
            name='link',
            field=models.CharField(max_length=50, null=True, verbose_name='Identifier'),
        ),
    ]
