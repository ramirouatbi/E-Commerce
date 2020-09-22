# Generated by Django 3.1.1 on 2020-09-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_orderitem_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='store.NewOrderItem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]