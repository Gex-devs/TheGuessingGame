# Generated by Django 3.0.3 on 2023-02-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230210_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualgame',
            name='subject',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
