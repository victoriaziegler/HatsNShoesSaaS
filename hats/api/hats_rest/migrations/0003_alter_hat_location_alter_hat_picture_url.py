# Generated by Django 4.0.3 on 2022-07-28 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0002_alter_hat_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hat',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='hats_rest.locationvo'),
        ),
        migrations.AlterField(
            model_name='hat',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
