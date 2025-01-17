# Generated by Django 3.1.1 on 2020-09-18 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueryHash',
            fields=[
                ('query_param_hash', models.IntegerField(primary_key=True, serialize=False)),
                ('question_ids', models.CharField(blank=True, max_length=500)),
                ('has_more', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShallowUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('reputation', models.IntegerField(null=True)),
                ('display_name', models.CharField(blank=True, max_length=200)),
                ('profile_image', models.CharField(blank=True, max_length=300)),
                ('link', models.CharField(blank=True, max_length=300)),
                ('user_type', models.CharField(choices=[('unregistered', 'unregistered'), ('registered', 'registered'), ('moderator', 'moderator'), ('team_admin', 'team_admin'), ('does_not_exist', 'does_not_exist')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_answered', models.BooleanField(blank=True)),
                ('view_count', models.IntegerField(null=True)),
                ('answer_count', models.IntegerField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('last_activity_date', models.IntegerField(null=True)),
                ('creation_date', models.IntegerField(null=True)),
                ('content_license', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('link', models.CharField(blank=True, max_length=300)),
                ('tags', models.CharField(blank=True, max_length=200)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='searcher.shallowuser')),
            ],
        ),
    ]
