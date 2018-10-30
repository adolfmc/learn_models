# Generated by Django 2.1.2 on 2018-10-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='perduct',
            name='s31',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='perduct',
            name='s32',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
