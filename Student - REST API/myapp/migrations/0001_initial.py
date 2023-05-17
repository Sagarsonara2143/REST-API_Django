# Generated by Django 4.2.1 on 2023-05-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=100)),
                ('lname', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('address', models.CharField(blank=True, max_length=100)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('fees', models.PositiveIntegerField()),
            ],
        ),
    ]
