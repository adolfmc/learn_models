# Generated by Django 2.1.2 on 2018-10-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(max_length=300)),
                ('s2', models.CharField(max_length=300)),
                ('s3', models.CharField(max_length=300)),
                ('s4', models.CharField(max_length=300)),
                ('s5', models.CharField(max_length=300)),
                ('s6', models.CharField(max_length=300)),
                ('s7', models.CharField(max_length=300)),
                ('s8', models.CharField(max_length=300)),
                ('s9', models.CharField(max_length=300)),
                ('s10', models.CharField(max_length=300)),
                ('s11', models.CharField(max_length=300)),
                ('s12', models.CharField(max_length=300)),
                ('s13', models.CharField(max_length=300)),
                ('s14', models.CharField(max_length=300)),
                ('s15', models.CharField(max_length=300)),
                ('s16', models.CharField(max_length=300)),
                ('s17', models.CharField(max_length=300)),
                ('s18', models.CharField(max_length=300)),
                ('s19', models.CharField(max_length=300)),
                ('s20', models.CharField(max_length=300)),
                ('s21', models.CharField(max_length=300)),
                ('s22', models.CharField(max_length=300)),
                ('s23', models.CharField(max_length=300)),
                ('s24', models.CharField(max_length=300)),
                ('s25', models.CharField(max_length=300)),
                ('s26', models.CharField(max_length=300)),
                ('s27', models.CharField(max_length=300)),
                ('s28', models.CharField(max_length=300)),
                ('s29', models.CharField(max_length=300)),
                ('s30', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
