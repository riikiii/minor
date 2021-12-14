# Generated by Django 3.1.5 on 2021-09-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0002_auto_20210923_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(choices=[('blood donor', 'blood donor'), ('organ donor', 'organ donor'), ('organ recipient', 'organ recipient'), ('volunteer', 'volunteer')], max_length=100, null=True),
        ),
    ]
