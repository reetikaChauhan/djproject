# Generated by Django 2.2.3 on 2019-08-21 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_tb_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=225)),
                ('Job_title', models.CharField(max_length=225)),
                ('Specialization', models.CharField(max_length=225)),
                ('experience', models.CharField(max_length=225)),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.tb_registration')),
            ],
        ),
    ]