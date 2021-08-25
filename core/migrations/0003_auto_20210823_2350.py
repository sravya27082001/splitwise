# Generated by Django 3.2.6 on 2021-08-23 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_event_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='groupAdmin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='DebtAdmin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='groupAdmin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='EventAdmin', to=settings.AUTH_USER_MODEL),
        ),
    ]
