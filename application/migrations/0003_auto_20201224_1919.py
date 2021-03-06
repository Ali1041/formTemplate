# Generated by Django 3.1.4 on 2020-12-24 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20201224_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='birth_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth_country', to='application.country'),
        ),
        migrations.AlterField(
            model_name='record',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='application.country'),
        ),
    ]
