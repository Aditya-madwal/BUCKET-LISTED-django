# Generated by Django 4.2.7 on 2024-01-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_item_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.CharField(max_length=1000),
        ),
    ]
