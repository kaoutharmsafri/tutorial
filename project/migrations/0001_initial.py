# Generated by Django 4.1.7 on 2023-02-21 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_d_operation', models.DateField()),
                ('Total_Credit', models.FloatField()),
                ('Date_d_echeance', models.DateField()),
                ('Etat', models.BooleanField()),
                ('Avance', models.FloatField()),
                ('Nom_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
            ],
        ),
        migrations.CreateModel(
            name='Epicerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Epicerie', models.CharField(max_length=255)),
                ('Adresse_Epicerie', models.CharField(max_length=255)),
                ('Tel_Epicerie', models.CharField(max_length=10)),
                ('Nom_Epicier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.epicier')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description_Produit', models.CharField(max_length=250)),
                ('Prix_Produit', models.FloatField()),
                ('Disponibilité', models.BooleanField()),
                ('Nom_Epicerie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.epicerie')),
            ],
        ),
        migrations.CreateModel(
            name='DetailsCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantite', models.IntegerField()),
                ('Total', models.FloatField()),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.credit')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.produit')),
            ],
        ),
        migrations.AddField(
            model_name='credit',
            name='Nom_Epicerie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.epicerie'),
        ),
    ]
