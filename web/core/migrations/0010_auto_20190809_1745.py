# Generated by Django 2.2.4 on 2019-08-09 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_birth_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='flower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.Flower'),
        ),
    ]
