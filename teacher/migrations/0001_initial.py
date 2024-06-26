# Generated by Django 5.0.6 on 2024-06-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=50)),
                ('hire_date', models.DateField()),
                ('is_fulltime', models.BooleanField(default=True)),
                ('office_number', models.CharField(max_length=10)),
                ('subjects_taught', models.TextField()),
            ],
        ),
    ]
