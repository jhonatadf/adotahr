# Generated by Django 5.1.1 on 2024-09-13 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0002_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='fotos_pets')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=14)),
                ('status', models.CharField(choices=[('P', 'Para adoção'), ('A', 'Adotado')], default='P', max_length=1)),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='divulgar.raca')),
                ('tags', models.ManyToManyField(to='divulgar.tag')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]