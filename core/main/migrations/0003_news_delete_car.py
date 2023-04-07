# Generated by Django 4.0.6 on 2022-07-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_car_slug_alter_car_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Car name')),
                ('title_hy', models.CharField(max_length=50, null=True, verbose_name='Car name')),
                ('title_ru', models.CharField(max_length=50, null=True, verbose_name='Car name')),
                ('title_en', models.CharField(max_length=50, null=True, verbose_name='Car name')),
                ('text', models.TextField(verbose_name='Car text')),
                ('text_hy', models.TextField(null=True, verbose_name='Car text')),
                ('text_ru', models.TextField(null=True, verbose_name='Car text')),
                ('text_en', models.TextField(null=True, verbose_name='Car text')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]