# Generated by Django 5.1.1 on 2024-10-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.CharField(null=True)),
                ('end_date', models.CharField(blank=True, null=True)),
                ('duration', models.TextField(null=True)),
            ],
        ),
    ]
