# Generated by Django 4.1.7 on 2023-02-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('designation', models.CharField(default='', max_length=20)),
                ('salary', models.IntegerField(default='0')),
                ('Face_book', models.CharField(default='', max_length=30)),
                ('Twitter', models.CharField(default='', max_length=30)),
                ('Instagram', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]
