# Generated by Django 2.2.3 on 2019-07-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mammadovsapp', '0008_auto_20190715_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
