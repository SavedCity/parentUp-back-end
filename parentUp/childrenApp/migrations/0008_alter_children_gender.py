# Generated by Django 4.0.2 on 2022-02-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenApp', '0007_children_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='gender',
            field=models.CharField(choices=[(1, 'Boy'), (2, 'Girl')], default='Boy', max_length=4),
        ),
    ]
