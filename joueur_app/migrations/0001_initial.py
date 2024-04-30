# Generated by Django 5.0.4 on 2024-04-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arena_app', '0001_initial'),
        ('pokemon_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('argent', models.IntegerField()),
                ('password', models.CharField(max_length=128)),
                ('badges', models.ManyToManyField(blank=True, to='arena_app.badge')),
                ('pokemons', models.ManyToManyField(blank=True, to='pokemon_app.pokemon')),
            ],
        ),
    ]
