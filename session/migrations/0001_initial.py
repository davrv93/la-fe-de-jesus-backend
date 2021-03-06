# Generated by Django 2.2.12 on 2020-05-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id_session', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('order', models.IntegerField()),
                ('translate_key', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='')),
                ('router', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
