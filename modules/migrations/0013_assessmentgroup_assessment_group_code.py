# Generated by Django 2.2 on 2019-12-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0012_auto_20191128_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentgroup',
            name='assessment_group_code',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
