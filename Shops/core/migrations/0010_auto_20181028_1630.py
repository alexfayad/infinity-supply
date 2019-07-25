# Generated by Django 2.1.2 on 2018-10-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20181028_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='shop_name',
            field=models.TextField(choices=[('STUSSY', 'Stussy'), ('FILA', 'Fila'), ('KAPPA', 'Kappa'), ('TOMMY', 'Tommy Hilifiger'), ('CK', 'Calvin Klein'), ('GUESS', 'Guess'), ('FRED_PERRY', 'Fred Perry'), ('VANS', 'Vans'), ('NIKE', 'Nike '), ('ADIDAS', 'Adidas'), ('REEBOK', 'Reebok'), ('ALLSAINTS', 'All Saints'), ('HM', 'H&M'), ('RALPH_LAUREN', 'Ralph Lauren '), ('TOPMAN', 'Topman'), ('CHAMPION', 'Champion')], null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('pants', 'pants'), ('eyewear', 'eyewear'), ('long-sleeves', 'long-sleeves'), ('tank-tops', 'tank-tops'), ('wallets', 'wallets'), ('other', 'other'), ('bombers', 'bombers'), ('thongs', 'thongs'), ('hats', 'hats'), ('sweatpants', 'sweatpants'), ('gloves', 'gloves'), ('scarves', 'scarves'), ('dress-shirt', 'dress-shirt'), ('sweatshirts', 'sweatshirts'), ('boxers', 'boxers'), ('bras', 'bras'), ('jackets', 'jackets'), ('loafers', 'loafers'), ('turtlenecks', 'turtlenecks'), ('jeans', 'jeans'), ('socks', 'socks'), ('coats', 'coats'), ('polo', 'polo'), ('shorts', 'shorts'), ('formal-wear', 'formal-wear'), ('blazers', 'blazers'), ('joggers', 'joggers'), ('sneakers', 'sneakers'), ('belts', 'belts'), ('corsets-and-bodysuits', 'corsets-and-bodysuits'), ('trousers', 'trousers'), ('vests', 'vests'), ('briefs', 'briefs'), ('crewnecks', 'crewnecks'), ('suits', 'suits'), ('cardigans', 'cardigans'), ('jewelry', 'jewelry'), ('t-shirt', 't-shirt'), ('dress-pants', 'dress-pants'), ('backpacks', 'backpacks'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups')], max_length=300, null=True),
        ),
    ]
