# Generated by Django 3.1.2 on 2020-10-20 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField()),
                ('name_animal', models.CharField(max_length=30)),
                ('number_of_limbs', models.IntegerField()),
                ('area', models.CharField(max_length=30)),
                ('life_style', models.CharField(max_length=30)),
                ('animal_class', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField()),
                ('date_cleaning', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('area_placements', models.CharField(max_length=255)),
                ('biom', models.CharField(max_length=255)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField()),
                ('staff_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('pay', models.IntegerField()),
                ('work_time_animal', models.IntegerField()),
                ('area_of_responsibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.placeanimal')),
                ('pinned_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField()),
                ('animal_group', models.CharField(max_length=30)),
                ('animal_family', models.CharField(max_length=30)),
                ('animal_type', models.CharField(max_length=30)),
                ('red_book', models.CharField(max_length=30)),
                ('animal_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.animal')),
            ],
        ),
    ]