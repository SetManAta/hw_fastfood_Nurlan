# Generated by Django 4.1.4 on 2022-12-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filial1', '0002_food_ingridient_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='card_number',
            field=models.IntegerField(),
        ),
        migrations.RemoveField(
            model_name='order',
            name='ingridient',
        ),
        migrations.AddField(
            model_name='order',
            name='ingridient',
            field=models.ManyToManyField(to='filial1.ingridient'),
        ),
    ]
