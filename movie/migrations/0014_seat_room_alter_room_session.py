# Generated by Django 4.1.3 on 2022-11-23 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0013_remove_seat_room_remove_session_room_room_session"),
    ]

    operations = [
        migrations.AddField(
            model_name="seat",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seats",
                to="movie.room",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="session",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="session_room",
                to="movie.session",
            ),
        ),
    ]
