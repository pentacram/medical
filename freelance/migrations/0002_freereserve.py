# Generated by Django 2.2.3 on 2019-08-07 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeReserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=None)),
                ('date', models.DateField()),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 – 10:00'), (1, '10:00 – 11:00'), (2, '11:00 – 12:00'), (3, '12:00 – 13:00'), (4, '13:00 – 14:00'), (5, '14:00 – 15:00'), (6, '15:00 – 16:00'), (7, '16:00 – 17:00'), (8, '17:00 – 18:00')])),
                ('contact_number', models.CharField(max_length=15)),
                ('comment', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.FreeDoctor')),
            ],
        ),
    ]
