# Generated by Django 5.2 on 2025-05-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='usertype',
            field=models.CharField(default='user', max_length=100),
        ),
    ]
