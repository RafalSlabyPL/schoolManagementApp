# Generated by Django 2.0.2 on 2018-05-25 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logowanie', '0008_auto_20180525_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlegrade',
            name='StudentsGrades',
        ),
        migrations.RemoveField(
            model_name='studentsgrades',
            name='student',
        ),
        migrations.AddField(
            model_name='course',
            name='studentsGrades',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logowanie.StudentsGrades'),
        ),
        migrations.AddField(
            model_name='studentsgrades',
            name='Student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logowanie.Student'),
        ),
        migrations.AddField(
            model_name='studentsgrades',
            name='StudentsGrades',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='logowanie.SingleGrade'),
        ),
    ]