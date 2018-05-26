# Generated by Django 2.0.2 on 2018-05-25 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logowanie', '0005_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=150)),
                ('teacherProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logowanie.PaymentHistory')),
            ],
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AlterField(
            model_name='admin',
            name='adminStatus',
            field=models.BooleanField(),
        ),
    ]
