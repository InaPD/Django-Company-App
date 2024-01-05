# Generated by Django 5.0.1 on 2024-01-04 19:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('number_of_employees', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
