# Generated by Django 4.2.1 on 2023-07-03 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_admin_table_admin_tables'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin_tables',
            new_name='admin_table',
        ),
    ]
