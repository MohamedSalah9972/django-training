# Generated by Django 4.0.4 on 2022-05-09 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('users', '0003_rename_user_myuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='CustomUser',
        ),
    ]
