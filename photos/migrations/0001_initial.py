# Generated by Django 3.2.3 on 2021-05-15 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_name', models.CharField(max_length=100)),
                ('image_description', models.TextField()),
                ('author', models.CharField(default='admin', max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.location')),
            ],
        ),
    ]
