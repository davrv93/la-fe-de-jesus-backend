# Generated by Django 2.2.12 on 2020-05-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='type',
            field=models.CharField(blank=True, choices=[('P', 'Preguntas'), ('S', 'Seccion')], max_length=1, null=True),
        ),
    ]
