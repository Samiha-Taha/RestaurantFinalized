# Generated by Django 4.1.7 on 2023-02-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodforall', '0003_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='review',
            field=models.CharField(max_length=150),
        ),
    ]
