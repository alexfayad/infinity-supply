# Generated by Django 2.1.2 on 2019-03-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20190320_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('formal-wear', 'formal-wear'), ('dress-shirt', 'dress-shirt'), ('t-shirt', 't-shirt'), ('boxers', 'boxers'), ('dress-pants', 'dress-pants'), ('polo', 'polo'), ('bras', 'bras'), ('wallets', 'wallets'), ('shorts', 'shorts'), ('gloves', 'gloves'), ('jackets', 'jackets'), ('briefs', 'briefs'), ('sweatpants', 'sweatpants'), ('vests', 'vests'), ('loafers', 'loafers'), ('suits', 'suits'), ('joggers', 'joggers'), ('socks', 'socks'), ('turtlenecks', 'turtlenecks'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups'), ('corsets-and-bodysuits', 'corsets-and-bodysuits'), ('jeans', 'jeans'), ('hats', 'hats'), ('thongs', 'thongs'), ('crewnecks', 'crewnecks'), ('coats', 'coats'), ('backpacks', 'backpacks'), ('pants', 'pants'), ('blazers', 'blazers'), ('other', 'other'), ('belts', 'belts'), ('sweatshirts', 'sweatshirts'), ('trousers', 'trousers'), ('sneakers', 'sneakers'), ('jewelry', 'jewelry'), ('eyewear', 'eyewear'), ('tank-tops', 'tank-tops'), ('long-sleeves', 'long-sleeves'), ('bombers', 'bombers'), ('cardigans', 'cardigans'), ('scarves', 'scarves')], max_length=300, null=True),
        ),
    ]
