# Generated by Django 5.1.1 on 2024-09-13 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
    ]
