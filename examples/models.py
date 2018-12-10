from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


# Create your models here.

class Validated(models.Model):
    """
    Shows validation capabilities
    """
    code = models.CharField(max_length=10, validators=[
        RegexValidator(r'\w\w\d+', 'Please enter a string starting with two characters, followed by up to 8 numbers')
    ])
    enabled = models.BooleanField()
    amount = models.IntegerField(null=True, blank=True, validators=[
        # This one should be interesting: will a blank value pass the Min validator? It should!
        MinValueValidator(5),
        MaxValueValidator(10)
    ])  # Bit mask. 1=apartment_number, ..., 32=delay
    item_type = models.IntegerField(choices=(
        (0, 'Choice 1'),
        (1, 'Choice 2'),
        (2, 'Choice 3'),
        (3, 'Choice 4'),
    ))
    item_flags = models.CharField(max_length=4, blank=True, choices=(
        # this one will be a multi-choice field so you will need to override it in form
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ), validators=[
        RegexValidator(r'^[ABC]*$', 'Only options A-C may be chosen', 'regex')
    ])


class HiddenFields(models.Model):
    """
    Shows dynamically changing field visibility
    """
    note = models.CharField(max_length=20, help_text='Enter abc to hide unit field')
    unit = models.CharField(max_length=10, choices=(
        ('pcs', 'Pieces'),
        ('wt', 'Weight'),
        ('cst', 'Custom'),
    ), null=True, blank=True)
    int_fld = models.IntegerField(verbose_name='Quantity', null=True, blank=True)
    qty_fld = models.FloatField(verbose_name='Weight', null=True, blank=True,
                                help_text='Fell free to use a decimal point / comma')
    cst_fld = models.CharField(max_length=80, verbose_name='Comment', null=True, blank=True,
                               help_text='Enter additional info here')
    additional_text = models.CharField(max_length=80, null=True, blank=True,
                                       help_text='Now that you have shown me, please enter something')


class PageLoad(models.Model):
    """
    Shows how DynamicForms handles dynamic loading of many records in ViewSet result
    """
    description = models.CharField(max_length=20, help_text='Item description')


class Filter(models.Model):
    """
    Shows how DynamicForms handles filers
    """
    char_field = models.CharField(max_length=20, help_text='Char field', verbose_name='Char field')
    datetime_field = models.DateTimeField(help_text='Datetime field', verbose_name='Datetime field')
    int_field = models.IntegerField(help_text='Integer field', verbose_name='Integer field')
    int_choice_field = models.IntegerField(choices=(
        (0, 'Choice 1'),
        (1, 'Choice 2'),
        (2, 'Choice 3'),
        (3, 'Choice 4'),), help_text='Integer field with choices', verbose_name='Integer field with choices')
    bool_field = models.BooleanField(help_text='Boolean field', verbose_name='Boolean field')
