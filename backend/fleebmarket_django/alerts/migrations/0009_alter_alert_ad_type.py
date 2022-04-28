# Generated by Django 3.2.2 on 2021-12-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0008_auto_20210825_1655"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alert",
            name="ad_type",
            field=models.CharField(
                choices=[
                    ("Selling", "Selling"),
                    ("Buying", "Buying"),
                    ("Trading", "Trading"),
                    ("Giveaway", "Giveaway"),
                    ("Group_buy", "Group Buy"),
                    ("Any", "Any"),
                ],
                max_length=30,
            ),
        ),
    ]
