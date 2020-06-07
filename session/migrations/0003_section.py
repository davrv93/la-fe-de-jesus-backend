# Generated by Django 2.2.12 on 2020-05-03 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_session_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id_section', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('order', models.IntegerField()),
                ('translate_key', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='')),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.ForeignKey(db_column='id_session', on_delete=django.db.models.deletion.PROTECT, to='session.Session')),
            ],
        ),
    ]
