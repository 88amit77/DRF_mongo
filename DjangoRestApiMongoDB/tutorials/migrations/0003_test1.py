# Generated by Django 3.0.5 on 2021-05-23 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
