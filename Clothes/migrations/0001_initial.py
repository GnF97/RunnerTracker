# Generated by Django 3.2.6 on 2021-09-01 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameB', models.CharField(choices=[('N', 'Nike'), ('As', 'Asics'), ('Ad', 'Adidas'), ('Sa', 'Salomon'), ('Ho', 'HokaOneOne')], default='N', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clothets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='')),
                ('nameC', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Targets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameT', models.CharField(choices=[('Esy', 'Easy'), ('Tmp', 'Tempo'), ('Lng', 'Long')], default='Esy', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameS', models.CharField(max_length=20)),
                ('surface', models.CharField(choices=[('Trl', 'Trail'), ('Rd', 'Road')], default='Rd', max_length=10)),
                ('milage', models.FloatField(max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clothes.brands')),
                ('target', models.ManyToManyField(to='Clothes.Targets')),
            ],
        ),
        migrations.CreateModel(
            name='Runs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mileage', models.FloatField(max_length=3)),
                ('duration', models.DateTimeField(blank=True)),
                ('pace', models.IntegerField(max_length=3)),
                ('runner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Clothes.clothets')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clothes.shoes')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clothes.targets')),
            ],
        ),
        migrations.AddField(
            model_name='clothets',
            name='shoe',
            field=models.ManyToManyField(to='Clothes.Shoes'),
        ),
        migrations.AddField(
            model_name='clothets',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
