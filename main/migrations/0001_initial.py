# Generated by Django 4.1.3 on 2022-12-06 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("item_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_name", models.CharField(max_length=100)),
                ("time_found", models.DateTimeField(auto_now_add=True)),
                ("where_found", models.CharField(max_length=100)),
                ("where_left", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=1000)),
                ("image", models.FileField(upload_to="items/")),
                ("time_claimed", models.DateTimeField(blank=True, null=True)),
                ("status", models.CharField(max_length=50)),
                (
                    "claim_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="claim",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "curr_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="curr",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
