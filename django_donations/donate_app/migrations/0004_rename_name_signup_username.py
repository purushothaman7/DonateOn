# Generated by Django 4.2.4 on 2023-09-05 17:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("donate_app", "0003_remove_signup_city"),
    ]

    operations = [
        migrations.RenameField(
            model_name="signup",
            old_name="name",
            new_name="username",
        ),
    ]