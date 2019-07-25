# Generated by Django 2.1.2 on 2018-10-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181028_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop_name',
            field=models.TextField(choices=[('STUSSY', 'Stussy'), ('FILA', 'Fila'), ('KAPPA', 'Kappa'), ('TOMMY', 'Tommy Hilifiger'), ('CK', 'Calvin Klein'), ('GUESS', 'Guess'), ('FRED_PERRY', 'Fred Perry'), ('VANS', 'Vans'), ('NIKE', 'Nike '), ('ADIDAS', 'Adidas'), ('REEBOK', 'Reebok'), ('ALLSAINTS', 'All Saints'), ('HM', 'H&M'), ('RALPH_LAUREN', 'Ralph Lauren '), ('TOPMAN', 'Topman'), ('CHAMPION', 'Champion'), ('ZARA', 'Zara')], default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='shop_name',
            field=models.TextField(choices=[('STUSSY', 'Stussy'), ('FILA', 'Fila'), ('KAPPA', 'Kappa'), ('TOMMY', 'Tommy Hilifiger'), ('CK', 'Calvin Klein'), ('GUESS', 'Guess'), ('FRED_PERRY', 'Fred Perry'), ('VANS', 'Vans'), ('NIKE', 'Nike '), ('ADIDAS', 'Adidas'), ('REEBOK', 'Reebok'), ('ALLSAINTS', 'All Saints'), ('HM', 'H&M'), ('RALPH_LAUREN', 'Ralph Lauren '), ('TOPMAN', 'Topman'), ('CHAMPION', 'Champion'), ('ZARA', 'Zara')], null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('formal-wear', 'formal-wear'), ('jackets', 'jackets'), ('cardigans', 'cardigans'), ('sweatshirts', 'sweatshirts'), ('sweatpants', 'sweatpants'), ('gloves', 'gloves'), ('long-sleeves', 'long-sleeves'), ('t-shirt', 't-shirt'), ('pants', 'pants'), ('boxers', 'boxers'), ('socks', 'socks'), ('dress-pants', 'dress-pants'), ('trousers', 'trousers'), ('polo', 'polo'), ('scarves', 'scarves'), ('backpacks', 'backpacks'), ('other', 'other'), ('suits', 'suits'), ('jewelry', 'jewelry'), ('coats', 'coats'), ('eyewear', 'eyewear'), ('turtlenecks', 'turtlenecks'), ('joggers', 'joggers'), ('blazers', 'blazers'), ('crewnecks', 'crewnecks'), ('vests', 'vests'), ('wallets', 'wallets'), ('belts', 'belts'), ('dress-shirt', 'dress-shirt'), ('sneakers', 'sneakers'), ('bombers', 'bombers'), ('shorts', 'shorts'), ('jeans', 'jeans'), ('loafers', 'loafers'), ('bras', 'bras'), ('tank-tops', 'tank-tops'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups'), ('thongs', 'thongs'), ('hats', 'hats'), ('briefs', 'briefs'), ('corsets-and-bodysuits', 'corsets-and-bodysuits')], max_length=300, null=True),
        ),
    ]
