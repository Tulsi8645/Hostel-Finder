# Generated by Django 4.1.6 on 2023-02-13 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sub',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hostel_name', models.CharField(max_length=200)),
                ('hostel_type', models.CharField(choices=[('boy', 'Boy'), ('girl', 'Girl')], max_length=10)),
                ('pan_no', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('manager_name', models.CharField(max_length=100)),
                ('manager_contact', models.CharField(max_length=100)),
                ('single_seater', models.IntegerField(blank=True, null=True)),
                ('two_seater', models.IntegerField(blank=True, null=True)),
                ('three_seater', models.IntegerField(blank=True, null=True)),
                ('four_seater', models.IntegerField(blank=True, null=True)),
                ('admission_fee', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('image_1', models.URLField(blank=True, null=True)),
                ('image_2', models.URLField(blank=True, null=True)),
                ('image_3', models.URLField(blank=True, null=True)),
                ('wifi', models.BooleanField(default=False)),
                ('closet', models.BooleanField(default=False)),
                ('hot_water', models.BooleanField(default=False)),
                ('laundry', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=False)),
                ('fan', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('map_link', models.URLField(blank=True, null=True)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostel', to='api.user')),
            ],
        ),
    ]
