# Generated by Django 3.0 on 2020-10-24 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idGenero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genero.Genero')),
            ],
        ),
    ]
