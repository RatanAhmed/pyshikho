# Generated by Django 2.0.3 on 2023-06-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_questions_learn_or_practice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('slug', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('codes', models.TextField(null=True)),
                ('search_count', models.IntegerField(null=True)),
                ('is_input_required', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
