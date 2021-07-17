# Generated by Django 3.0.5 on 2021-05-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]