# Generated by Django 4.0.2 on 2022-02-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenApp', '0013_alter_children_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='gender',
            field=models.CharField(choices=[(1, 'Boy'), (2, 'Girl')], default=1, max_length=4),
        ),
    ]
