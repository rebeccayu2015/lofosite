# Generated by Django 4.1.3 on 2023-03-07 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0003_alter_item_claim_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="curr_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="curr_item",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Missing",
            fields=[
                ("item_id", models.AutoField(primary_key=True, serialize=False)),
                ("item_name", models.CharField(max_length=100)),
                ("time_posted", models.DateTimeField(auto_now_add=True)),
                ("last_seen", models.DateTimeField(blank=True, null=True)),
                ("description", models.TextField(max_length=1000)),
                ("status", models.CharField(max_length=50)),
                (
                    "curr_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="curr_missing",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]