# Generated by Django 2.0.2 on 2020-07-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('reference_number', models.BigIntegerField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('url', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('register_date', models.TextField(blank=True, null=True)),
                ('open_days', models.BigIntegerField(blank=True, null=True)),
                ('quantity', models.BigIntegerField(blank=True, null=True)),
                ('job_type', models.TextField(blank=True, null=True)),
                ('study', models.IntegerField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('work_time', models.TextField(blank=True, null=True)),
                ('salary', models.TextField(blank=True, null=True)),
                ('salary_type', models.TextField(blank=True, null=True)),
                ('workplace', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.IntegerField(blank=True, null=True)),
                ('picker', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vagas',
                'managed': True,
            },
        ),
    ]
