# Generated by Django 2.1.5 on 2019-02-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190225_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table_number',
            field=models.CharField(choices=[('t1', 't1'), ('t2', 't2'), ('t3', 't3')], max_length=30),
        ),
    ]