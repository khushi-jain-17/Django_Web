# Generated by Django 5.1.1 on 2024-10-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_profile_blood_group_alter_profile_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=100)),
            ],
        ),
    ]
