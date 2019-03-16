# Generated by Django 2.1 on 2018-09-01 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50)),
                ('avatar_url', models.URLField()),
                ('html_url', models.URLField()),
                ('_type', models.CharField(choices=[('users', 'Usuario'), ('orgs', 'Organizacion')], default='users', max_length=5)),
                ('total_repos', models.PositiveSmallIntegerField(default=0)),
                ('ultima_consulta', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repos',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('fork', models.BooleanField(default=False)),
                ('html_url', models.URLField()),
                ('description', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField()),
                ('pushed_at', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Owner')),
            ],
        ),
    ]
