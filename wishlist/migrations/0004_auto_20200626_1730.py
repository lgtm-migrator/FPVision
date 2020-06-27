# Generated by Django 3.0.7 on 2020-06-26 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0013_auto_20200617_0820'),
        ('wishlist', '0003_remove_wishlist_wishlist_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='wished_product',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('wishlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlistitems', to='wishlist.Wishlist')),
            ],
        ),
    ]
