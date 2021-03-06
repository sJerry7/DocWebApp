# Generated by Django 3.0.5 on 2020-05-30 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dr_name', models.CharField(max_length=80)),
                ('dr_img', models.ImageField(upload_to='pics')),
                ('dr_qualification', models.CharField(max_length=40)),
                ('dr_address', models.CharField(max_length=254)),
                ('dr_city', models.CharField(max_length=30)),
                ('dr_email', models.EmailField(max_length=254)),
                ('dr_mobile', models.TextField()),
                ('dr_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.CategoryTable')),
            ],
        ),
    ]
