# Generated by Django 2.1.2 on 2019-08-02 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0022_auto_20190320_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('dress-shirt', 'dress-shirt'), ('thongs', 'thongs'), ('corsets-and-bodysuits', 'corsets-and-bodysuits'), ('crewnecks', 'crewnecks'), ('jewelry', 'jewelry'), ('polo', 'polo'), ('vests', 'vests'), ('loafers', 'loafers'), ('briefs', 'briefs'), ('wallets', 'wallets'), ('trousers', 'trousers'), ('t-shirt', 't-shirt'), ('blazers', 'blazers'), ('boxers', 'boxers'), ('tank-tops', 'tank-tops'), ('long-sleeves', 'long-sleeves'), ('gloves', 'gloves'), ('dress-pants', 'dress-pants'), ('turtlenecks', 'turtlenecks'), ('jeans', 'jeans'), ('bras', 'bras'), ('coats', 'coats'), ('jackets', 'jackets'), ('pants', 'pants'), ('sweatshirts', 'sweatshirts'), ('formal-wear', 'formal-wear'), ('backpacks', 'backpacks'), ('cardigans', 'cardigans'), ('hats', 'hats'), ('bombers', 'bombers'), ('eyewear', 'eyewear'), ('joggers', 'joggers'), ('shorts', 'shorts'), ('other', 'other'), ('belts', 'belts'), ('suits', 'suits'), ('sweatpants', 'sweatpants'), ('sneakers', 'sneakers'), ('scarves', 'scarves'), ('socks', 'socks'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups')], max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
