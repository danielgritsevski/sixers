# Generated by Django 2.1.5 on 2019-02-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('new', 'new'), ('delivery', 'delivery'), ('finished', 'finished'), ('aborted', 'aborted')], default='new', max_length=24),
        ),
    ]