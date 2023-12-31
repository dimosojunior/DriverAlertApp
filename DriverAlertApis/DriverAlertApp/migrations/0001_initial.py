# Generated by Django 4.2.2 on 2023-07-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewsName', models.CharField(max_length=200)),
                ('NewNews', models.TextField(blank=True, max_length=1000, null=True)),
                ('NewsDescription', models.TextField(blank=True, max_length=10000, null=True)),
                ('EventLatitude', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('EventLongitude', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LatitudeArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LongitudeArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LatitudeDeltaArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LongitudeDeltaArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('NewsImage', models.ImageField(blank=True, null=True, upload_to='media/NewsEEventImage/')),
                ('NewsDate', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'NewsEvent',
            },
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RouteName', models.CharField(max_length=200)),
                ('NewNews', models.TextField(blank=True, max_length=1000, null=True)),
                ('RouteDescription', models.TextField(blank=True, max_length=10000, null=True)),
                ('EventLatitude', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('EventLongitude', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LatitudeArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LongitudeArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LatitudeDeltaArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('LongitudeDeltaArea', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('RouteImage', models.ImageField(blank=True, null=True, upload_to='media/RoutesImage/')),
                ('NewsDate', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Routes',
            },
        ),
    ]
