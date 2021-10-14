# Generated by Django 3.2.8 on 2021-10-12 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('charge_cost', models.PositiveSmallIntegerField(default=1)),
                ('charges', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('does_recharge', models.BooleanField(default=False)),
                ('is_ranged', models.BooleanField(default=False)),
                ('recharge_time', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ItemEffectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemSpecialProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSubtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpgcore.itemtype')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_equipped', models.BooleanField(default=False)),
                ('special_properties', models.ManyToManyField(blank=True, to='rpgcore.ItemSpecialProperties')),
            ],
        ),
        migrations.CreateModel(
            name='ItemEffect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect_amount', models.SmallIntegerField(default=0)),
                ('effect_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpgcore.itemeffecttype')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpgcore.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='properties',
            field=models.ManyToManyField(blank=True, to='rpgcore.ItemProperty'),
        ),
        migrations.AddField(
            model_name='item',
            name='subtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpgcore.itemsubtype'),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rpgcore.itemtype'),
        ),
    ]
