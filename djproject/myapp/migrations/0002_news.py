# Generated by Django 2.2.3 on 2019-08-19 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('authors', models.CharField(max_length=225)),
                ('publication_date', models.DateField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.web1')),
            ],
        ),
    ]
