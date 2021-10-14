from django.db import models
from django.db.models.functions import Upper

class Item(models.Model):
    class Meta:
        ordering = [Upper('name')]
    name = models.CharField(
        max_length=100,
        unique=True)
    # charge_cost = models.PositiveSmallIntegerField(default=1)
    # charges = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(
        default='',
        blank=True)
    # does_recharge = models.BooleanField(default=False)
    is_equippable = models.BooleanField(default=False)
    # is_ranged = models.BooleanField(default=False)
    properties = models.ManyToManyField(
        'ItemProperty',
        blank=True)
    type = models.ForeignKey(
        'ItemType',
        null=True,
        on_delete=models.SET_NULL)
    subtype = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    # recharge_time = models.PositiveIntegerField(default=0)
    # icon
    # user
    # created_on
    # edited_on

    def __str__(self):
        return self.name


class ItemEffect(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE)
    effect_amount = models.SmallIntegerField(default=0)
    effect_type = models.ForeignKey(
        'ItemEffectType',
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.effect_amount}: {self.effect_type}'


class ItemEffectType(models.Model):
    class Meta:
        ordering = [Upper('name')]
    name = models.CharField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.name


class ItemInstance(models.Model):
    class Meta:
        ordering = [Upper('name')]
    name = models.CharField(max_length=100, blank=True) # Should default to item name if blank
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_equipped = models.BooleanField(default=False)
    # owner = models.ForeignKey(Character)
    special_properties = models.ManyToManyField(
        'ItemSpecialProperty',
        blank=True)

    def __str__(self):
        return self.name # join self.special_properties


class ItemProperty(models.Model):
    class Meta:
        ordering = [Upper('name')]
    name = models.CharField(
        max_length=50,
        unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ItemSpecialProperty(models.Model):
    class Meta:
        ordering = [Upper('name')]
    name = models.CharField(
        max_length=50)
    description = models.TextField()
    requirements = models.ManyToManyField(
        ItemProperty,
        blank=True)

    def __str__(self):
        return self.name


class ItemType(models.Model):
    class Meta:
        ordering = [Upper('name')]
    name = models.CharField(
        max_length=50,
        unique=True)

    def __str__(self):
        return self.name
