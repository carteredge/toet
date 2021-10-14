# Generated by Django 3.2.8 on 2021-10-14 14:34

from django.db import migrations
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('rpgcore', '0006_alter_item_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemeffecttype',
            options={'ordering': [django.db.models.functions.text.Upper('name')]},
        ),
        migrations.AlterModelOptions(
            name='iteminstance',
            options={'ordering': [django.db.models.functions.text.Upper('name')]},
        ),
        migrations.AlterModelOptions(
            name='itemproperty',
            options={'ordering': [django.db.models.functions.text.Upper('name')]},
        ),
        migrations.AlterModelOptions(
            name='itemspecialproperty',
            options={'ordering': [django.db.models.functions.text.Upper('name')]},
        ),
        migrations.AlterModelOptions(
            name='itemtype',
            options={'ordering': [django.db.models.functions.text.Upper('name')]},
        ),
    ]
