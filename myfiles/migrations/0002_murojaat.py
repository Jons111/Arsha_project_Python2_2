# Generated by Django 4.1.4 on 2023-02-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murojaat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=40)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
