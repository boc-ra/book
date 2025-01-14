# Generated by Django 5.1.2 on 2024-11-14 07:16

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookdiaryForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日付')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('writer', models.CharField(max_length=40, verbose_name='作者')),
                ('text', models.CharField(max_length=200, verbose_name='本文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='編集日時')),
            ],
        ),
    ]
