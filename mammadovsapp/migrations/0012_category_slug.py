# Generated by Django 2.2.3 on 2019-07-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mammadovsapp', '0011_auto_20190720_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
