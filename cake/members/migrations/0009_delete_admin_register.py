# Generated by Django 4.2.1 on 2023-07-03 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_rename_admin_table_admin_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin_register',
        ),
    ]
