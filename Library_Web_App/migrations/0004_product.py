# Generated by Django 4.1.5 on 2023-01-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library_Web_App', '0003_book_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Is_Digital', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]