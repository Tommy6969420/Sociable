# Generated by Django 4.1.13 on 2024-02-16 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("upload_time", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="status/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Response",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("like_count", models.IntegerField(blank=True, default=0, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=20)),
                ("full_name", models.CharField(max_length=20)),
                ("contact_email", models.EmailField(max_length=254)),
                ("contact_number", models.CharField(max_length=15, unique=True)),
                ("date_of_birth", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="ResposePost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.post"
                    ),
                ),
                (
                    "response",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.response"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="response",
            name="responder",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
        ),
    ]