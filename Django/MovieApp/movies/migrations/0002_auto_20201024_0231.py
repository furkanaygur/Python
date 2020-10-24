# Generated by Django 3.1.2 on 2020-10-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isPublished',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='DESCRIPTION'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=255, verbose_name='IMAGE URL'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=255, verbose_name='NAME'),
        ),
    ]