# Generated by Django 3.2.9 on 2021-11-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250, unique=True)),
                ('is_true', models.BooleanField(default=True)),
            ],
        ),
    ]