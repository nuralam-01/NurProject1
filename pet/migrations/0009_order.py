# Generated by Django 5.0.1 on 2024-05-01 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0008_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Ordername', models.IntegerField(primary_key=True, serialize=False)),
                ('DateofOrder', models.DateTimeField()),
                ('Quantity', models.IntegerField()),
                ('Totalammount', models.IntegerField()),
                ('CompleteTrans', models.BooleanField()),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.addproduct')),
                ('Userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.users')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
    ]