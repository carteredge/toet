# Generated by Django 3.2.8 on 2021-10-13 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpgcore', '0003_auto_20211013_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='subtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpgcore.item'),
        ),
    ]
