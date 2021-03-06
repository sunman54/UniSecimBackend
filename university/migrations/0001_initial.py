# Generated by Django 4.0.5 on 2022-06-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Un',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.IntegerField(verbose_name=5)),
                ('type', models.TextField()),
                ('name', models.TextField()),
                ('faculty', models.TextField()),
                ('department', models.TextField()),
                ('point_type', models.TextField()),
                ('quota', models.IntegerField(verbose_name=5)),
                ('accepted', models.IntegerField(verbose_name=5)),
                ('min_point', models.IntegerField(verbose_name=5)),
                ('max_point', models.IntegerField(verbose_name=5)),
            ],
        ),
    ]
