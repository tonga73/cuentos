# Generated by Django 2.0.7 on 2018-10-11 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=100)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=100)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='cuento',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuentos', to='blog.Publicacion'),
        ),
    ]
