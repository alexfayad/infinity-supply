# Generated by Django 2.1.2 on 2019-02-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20190203_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_from', models.TextField()),
                ('currency_to', models.TextField()),
                ('value', models.DecimalField(decimal_places=3, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('wallets', 'wallets'), ('belts', 'belts'), ('corsets-and-bodysuits', 'corsets-and-bodysuits'), ('t-shirt', 't-shirt'), ('trousers', 'trousers'), ('sweatpants', 'sweatpants'), ('sneakers', 'sneakers'), ('loafers', 'loafers'), ('jeans', 'jeans'), ('suits', 'suits'), ('dress-shirt', 'dress-shirt'), ('jewelry', 'jewelry'), ('turtlenecks', 'turtlenecks'), ('sweatshirts', 'sweatshirts'), ('tank-tops', 'tank-tops'), ('bras', 'bras'), ('blazers', 'blazers'), ('socks', 'socks'), ('crewnecks', 'crewnecks'), ('boxers', 'boxers'), ('vests', 'vests'), ('long-sleeves', 'long-sleeves'), ('thongs', 'thongs'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups'), ('hats', 'hats'), ('shorts', 'shorts'), ('other', 'other'), ('bombers', 'bombers'), ('formal-wear', 'formal-wear'), ('pants', 'pants'), ('scarves', 'scarves'), ('eyewear', 'eyewear'), ('gloves', 'gloves'), ('dress-pants', 'dress-pants'), ('briefs', 'briefs'), ('coats', 'coats'), ('backpacks', 'backpacks'), ('jackets', 'jackets'), ('polo', 'polo'), ('joggers', 'joggers'), ('cardigans', 'cardigans')], max_length=300, null=True),
        ),
    ]
