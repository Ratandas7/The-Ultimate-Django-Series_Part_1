# Generated by Django 5.1.4 on 2024-12-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default='00000', max_length=20),
            preserve_default=False,
        ),
    ]
