# Generated by Django 5.1.4 on 2024-12-19 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondpi', '0004_rename_dpi_dpi_medecin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='resume',
        ),
        migrations.AddField(
            model_name='dpi',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/'),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostic', models.TextField(blank=True, null=True)),
                ('symptomes', models.TextField(blank=True, null=True)),
                ('antecedents', models.TextField(blank=True, null=True)),
                ('autres_informations', models.TextField(blank=True, null=True)),
                ('consultation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='gestiondpi.consultation')),
            ],
        ),
    ]