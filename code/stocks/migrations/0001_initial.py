# Generated by Django 3.1.2 on 2020-10-24 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('ticker', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceLookupEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('source', models.CharField(choices=[('business_insider', 'Business Insider Markets'), ('google_finance', 'Google Finance'), ('echo', 'Http Bin Echo')], default='echo', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stocks.company')),
            ],
        ),
    ]
