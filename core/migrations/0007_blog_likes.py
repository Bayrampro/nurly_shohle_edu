# Generated by Django 5.0.1 on 2024-01-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_blog_created_at_alter_blog_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
