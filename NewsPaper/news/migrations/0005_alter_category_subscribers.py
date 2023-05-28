# Generated by Django 4.2.1 on 2023-05-27 04:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_category_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
