# Generated by Django 4.2.6 on 2023-10-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderappp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
    ]
