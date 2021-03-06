# Generated by Django 3.1.4 on 2020-12-25 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20201224_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=49.0)),
                ('unit', models.CharField(default='USD', max_length=10)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('user_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to='application.record')),
            ],
        ),
    ]
