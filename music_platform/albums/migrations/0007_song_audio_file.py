# Generated by Django 4.0.3 on 2022-04-28 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_song_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default=1, upload_to='audio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]),
            preserve_default=False,
        ),
    ]
