# Generated by Django 2.2.3 on 2019-08-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('contact', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
            ],
        ),
    ]
