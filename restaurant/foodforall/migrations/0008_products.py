# Generated by Django 4.1.7 on 2023-02-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodforall', '0007_starters'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pict', models.ImageField(upload_to='img')),
                ('pro_name', models.CharField(max_length=20)),
                ('pro_desc', models.CharField(max_length=600)),
                ('pro_price', models.IntegerField()),
                ('pro_reviews', models.CharField(max_length=200)),
            ],
        ),
    ]
