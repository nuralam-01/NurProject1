# Generated by Django 5.0.1 on 2024-03-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0004_alter_addproduct_pimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
