# Generated by Django 3.2.21 on 2023-10-22 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labor',
            name='hours',
            field=models.FloatField(db_column='hours', verbose_name='Tempo:'),
        ),
        migrations.AlterField(
            model_name='labor',
            name='time',
            field=models.CharField(choices=[('Hora', 'Hora'), ('Minutos', 'Minutos'), ('Segundos', 'Segundos'), ('Dias', 'Dias')], max_length=15, verbose_name='Medida do Tempo:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, db_column='quantity', verbose_name='Quantidade Desejada (UNI):'),
        ),
        migrations.AlterField(
            model_name='product',
            name='taxes',
            field=models.FloatField(blank=True, db_column='taxes', verbose_name='Impostos %:'),
        ),
        migrations.CreateModel(
            name='PercentDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(db_column='percent', verbose_name='Porcentagem do Desconto:')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
            options={
                'ordering': ['percent'],
            },
        ),
    ]