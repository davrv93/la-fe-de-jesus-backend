# Generated by Django 2.2.12 on 2020-05-06 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0008_auto_20200506_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id_section', models.AutoField(primary_key=True, serialize=False)),
                ('chapter', models.IntegerField()),
                ('verse', models.IntegerField()),
                ('book', models.CharField(blank=True, max_length=300, null=True)),
                ('translate_key', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.BooleanField(default=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('chapter', 'verse'),
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='section',
            field=models.ForeignKey(db_column='id_section', on_delete=django.db.models.deletion.PROTECT, related_name='item_section_set', to='session.Section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='session',
            field=models.ForeignKey(db_column='id_session', on_delete=django.db.models.deletion.PROTECT, related_name='section_session_set', to='session.Session'),
        ),
        migrations.AddField(
            model_name='item',
            name='verse',
            field=models.ManyToManyField(related_name='item_verse_set', to='session.Verse'),
        ),
    ]
