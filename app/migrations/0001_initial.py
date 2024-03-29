# Generated by Django 4.2.6 on 2024-01-08 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sloc', models.CharField(max_length=100)),
                ('sprincipal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default=None, max_length=100)),
                ('DOB', models.DateField()),
                ('bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch')),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='sname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school'),
        ),
    ]
