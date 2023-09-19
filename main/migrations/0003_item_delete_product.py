# Generated by Django 4.2.5 on 2023-09-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
