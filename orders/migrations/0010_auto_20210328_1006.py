# Generated by Django 3.1.7 on 2021-03-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_orders_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='total',
        ),
        migrations.AddField(
            model_name='orders',
            name='items_ordered',
            field=models.ManyToManyField(related_name='items_ordered', to='orders.OrderItem'),
        ),
    ]