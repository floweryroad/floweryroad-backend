# Generated by Django 2.2.4 on 2019-08-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190809_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='season',
            field=models.IntegerField(choices=[(0, '봄'), (1, '여름'), (2, '가을'), (3, '겨울')], default=1),
        ),
    ]
