# Generated by Django 2.2.1 on 2019-06-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lap_type', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('issues', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
