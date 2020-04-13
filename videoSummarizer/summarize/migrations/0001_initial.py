# Generated by Django 3.0.5 on 2020-04-13 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Split',
            fields=[
                ('SplitID', models.AutoField(primary_key=True, serialize=False)),
                ('StartTime', models.IntegerField()),
                ('EndTime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('VideoID', models.AutoField(primary_key=True, serialize=False)),
                ('VideoPath', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SplitSummary',
            fields=[
                ('SplitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='summarize.Split')),
                ('SummaryPath', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SplitTranscript',
            fields=[
                ('SplitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='summarize.Split')),
                ('TranscriptPath', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSpeech',
            fields=[
                ('VideoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='summarize.Video')),
                ('SpeechPath', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSplit',
            fields=[
                ('VideoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='summarize.Video')),
                ('SplitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summarize.Split')),
            ],
        ),
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('VideoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='summarize.Video')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summarize.User')),
            ],
        ),
        migrations.CreateModel(
            name='SplitTag',
            fields=[
                ('SplitTagID', models.AutoField(primary_key=True, serialize=False)),
                ('Tag', models.CharField(max_length=50)),
                ('SplitID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summarize.Split')),
            ],
            options={
                'unique_together': {('SplitID', 'Tag')},
            },
        ),
    ]
