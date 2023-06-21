# Generated by Django 4.2.2 on 2023-06-21 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetings.room'),
            preserve_default=False,
        ),
    ]
