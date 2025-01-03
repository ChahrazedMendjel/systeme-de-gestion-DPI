# Generated by Django 5.1.4 on 2024-12-26 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestiondpi', '0014_alter_consultation_ordonnance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametrebiomesure',
            name='parametre_biologique',
        ),
        migrations.RemoveField(
            model_name='bilanbiologique',
            name='parametres',
        ),
        migrations.AddField(
            model_name='bilanbiologique',
            name='parametres_bio_mesures',
            field=models.ManyToManyField(related_name='bilans_biologiques', to='gestiondpi.parametrebiomesure'),
        ),
        migrations.AddField(
            model_name='parametrebiomesure',
            name='bilan_biologique',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='parametre_bio_mesures', to='gestiondpi.bilanbiologique'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametrebiomesure',
            name='nom',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametrebiomesure',
            name='unite_mesure',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametrebiomesure',
            name='valeur_normale',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ParametreBiologique',
        ),
    ]
