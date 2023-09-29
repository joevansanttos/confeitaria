# Generated by Django 3.2.21 on 2023-09-29 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('last_name', models.CharField(db_column='last', max_length=100)),
                ('job', models.CharField(db_column='job', max_length=100)),
                ('address', models.CharField(db_column='address', max_length=150)),
                ('city', models.CharField(db_column='city', max_length=100)),
                ('state', models.CharField(db_column='state', max_length=100)),
                ('phone', models.CharField(db_column='phone', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='Nome do Item:')),
                ('quantity', models.IntegerField(db_column='quantity', verbose_name='Quantidade do Pacote:')),
                ('measure', models.CharField(choices=[('KG', 'Kg'), ('GRAMAS', 'Gramas'), ('UNIDADES', 'Unidades')], max_length=8, verbose_name='Medida do Pacote:')),
                ('price', models.FloatField(db_column='price', verbose_name='(R$) Valor do Pacote:')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='Nome do Serviço:')),
                ('salary', models.FloatField(db_column='salary', verbose_name='Salário Médio:')),
                ('hours', models.FloatField(db_column='hours', verbose_name='Horas Mensais:')),
                ('time', models.CharField(choices=[('Hora', 'Hora'), ('Minutos', 'Minutos'), ('Segundos', 'Segundos'), ('Dias', 'Dias')], max_length=15, verbose_name='Tempo de Medida:')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='Nome do Item:')),
                ('quantity', models.IntegerField(db_column='quantity', verbose_name='Quantidade Comprada:')),
                ('price', models.FloatField(db_column='price', verbose_name='(R$) Preço do Pacote de Embalagem:')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('another_expenses', models.FloatField(blank=True, db_column='another_expenses', verbose_name='Outros Custos (R$):')),
                ('incalculable_expenses', models.FloatField(blank=True, db_column='incalculable_expenses', verbose_name='Custos Incalculáveis (R$):')),
                ('marketplace_tax', models.FloatField(blank=True, db_column='marketplace_tax', verbose_name='Taxa de Comissão em Marketplace (R$):')),
                ('taxes', models.FloatField(blank=True, db_column='taxes', verbose_name='Impostos:')),
                ('quantity', models.IntegerField(blank=True, db_column='quantity', verbose_name='Quantidade Desejada:')),
                ('profit', models.FloatField(blank=True, db_column='profit', verbose_name='Lucro Desejado (R$):')),
                ('labor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.labor')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PercentMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(db_column='percent', verbose_name='Quantidade Usada:')),
                ('material', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.material')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
            options={
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='PercentIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(db_column='percent', verbose_name='Quantidade Usada:')),
                ('measure', models.CharField(choices=[('KG', 'Kg'), ('GRAMAS', 'Gramas'), ('UNIDADES', 'Unidades')], max_length=8, verbose_name='Medida do Pacote:')),
                ('ingredient', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.ingredient')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
            options={
                'ordering': ['ingredient'],
            },
        ),
    ]
