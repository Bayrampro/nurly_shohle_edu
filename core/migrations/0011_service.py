# Generated by Django 5.0.1 on 2024-02-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Hyzmatyň ady')),
                ('content', models.TextField(blank=True, verbose_name='Hyzmat barada')),
            ],
        ),
    ]
