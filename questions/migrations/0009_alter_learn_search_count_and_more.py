# Generated by Django 4.2.5 on 2023-10-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_remove_questions_learn_or_practice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn',
            name='search_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_input_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='search_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
