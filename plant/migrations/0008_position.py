# Generated by Django 5.1.3 on 2024-12-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0007_alter_task_options_task_segment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
    ]
