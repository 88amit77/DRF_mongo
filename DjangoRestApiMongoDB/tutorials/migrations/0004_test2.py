# Generated by Django 3.0.5 on 2021-05-23 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_test1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]