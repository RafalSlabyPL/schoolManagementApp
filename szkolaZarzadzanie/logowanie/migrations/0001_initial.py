# Generated by Django 2.0.2 on 2018-05-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('region', models.CharField(blank=True, max_length=30)),
                ('postalCode', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
                ('homeNumber', models.IntegerField()),
                ('apartmentNumber', models.IntegerField(blank=True)),
                ('PESEL', models.IntegerField()),
            ],
        ),
    ]
