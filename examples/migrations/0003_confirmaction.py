# Generated by Django 2.2.1 on 2019-10-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0002_auto_20190320_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(help_text='Action name', max_length=256, verbose_name='Action name')),
                ('action_type', models.IntegerField(choices=[(0, 'Choice 1'), (1, 'Choice 2'), (2, 'Choice 3'), (3, 'Choice 4')])),
                ('enabled', models.BooleanField()),
            ],
        ),
    ]
