# Generated by Django 4.1.7 on 2023-02-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodforall', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagee', models.ImageField(upload_to='img')),
                ('review', models.CharField(max_length=50)),
            ],
        ),
    ]