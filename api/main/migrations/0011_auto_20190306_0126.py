# Generated by Django 2.1.5 on 2019-03-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190225_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='executionplan',
            options={'get_latest_by': 'created_at'},
        ),
        migrations.RemoveField(
            model_name='executionplan',
            name='plan_out',
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='main.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table_number',
            field=models.CharField(choices=[('t1', 't1'), ('t2', 't2'), ('t3', 't3'), ('t4', 't4')], max_length=30),
        ),
    ]
