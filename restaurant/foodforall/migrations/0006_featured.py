# Generated by Django 4.1.7 on 2023-02-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodforall', '0005_alter_testimonial_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='featured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='img')),
                ('dish_name', models.CharField(max_length=25)),
                ('dish_price', models.IntegerField()),
            ],
        ),
    ]