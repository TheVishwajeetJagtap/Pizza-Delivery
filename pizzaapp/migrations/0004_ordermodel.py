# Generated by Django 2.2.2 on 2020-07-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_customermodel_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('ordereditems', models.CharField(max_length=10)),
            ],
        ),
    ]