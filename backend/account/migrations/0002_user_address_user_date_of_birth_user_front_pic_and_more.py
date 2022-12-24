# Generated by Django 4.1.4 on 2022-12-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='front_pic',
            field=models.ImageField(blank=True, null=True, upload_to='verification'),
        ),
        migrations.AddField(
            model_name='user',
            name='id_num',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rear_pic',
            field=models.ImageField(blank=True, null=True, upload_to='verification'),
        ),
        migrations.DeleteModel(
            name='Verification',
        ),
    ]
