# Generated by Django 2.2.3 on 2019-08-20 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='web1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_head', models.CharField(max_length=255)),
                ('news_web', models.CharField(max_length=255)),
                ('news_img', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('authors', models.CharField(max_length=225)),
                ('publication_date', models.DateField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.web1')),
            ],
        ),
    ]