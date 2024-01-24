# Generated by Django 3.2.23 on 2024-01-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0011_auto_20240123_1934'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='vehicle',
            index=models.Index(fields=['year'], name='year_idx'),
        ),
        migrations.AddIndex(
            model_name='vehicle',
            index=models.Index(fields=['make'], name='make_idx'),
        ),
        migrations.AddIndex(
            model_name='vehicle',
            index=models.Index(fields=['model'], name='model_idx'),
        ),
    ]