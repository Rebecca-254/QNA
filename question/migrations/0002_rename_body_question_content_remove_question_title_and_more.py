# Generated by Django 5.2.4 on 2025-07-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='body',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
