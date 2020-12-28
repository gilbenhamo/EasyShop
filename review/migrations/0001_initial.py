# Generated by Django 3.1.4 on 2020-12-27 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicalcomments',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('comment', models.TextField(max_length=255)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - very bad'), (2, '2 - bad'), (3, '3 - OK'), (4, '4 - GOOD'), (5, '5 - Very Good')])),
                ('date', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('business_comments', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account.business')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical comments',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('comment', models.TextField(max_length=255)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - very bad'), (2, '2 - bad'), (3, '3 - OK'), (4, '4 - GOOD'), (5, '5 - Very Good')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('business_comments', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.business')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
