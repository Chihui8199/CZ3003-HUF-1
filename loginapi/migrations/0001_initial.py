# Generated by Django 3.2.7 on 2021-10-12 06:13

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
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
            name='HufGame',
            fields=[
                ('gameid', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(blank=True, max_length=20, null=True)),
                ('game_tag', models.CharField(max_length=9)),
                ('no_of_quiz', models.IntegerField()),
                ('game_description', models.CharField(blank=True, max_length=100, null=True)),
                ('total_no_qn', models.IntegerField()),
            ],
            options={
                'db_table': 'huf_game',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HufQuiz',
            fields=[
                ('quizid', models.IntegerField(primary_key=True, serialize=False)),
                ('quiz_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('quiz_max_score', models.IntegerField()),
                ('quiz_description', models.CharField(blank=True, max_length=50, null=True)),
                ('no_of_qn', models.IntegerField()),
                ('total_no_qn', models.IntegerField()),
            ],
            options={
                'db_table': 'huf_quiz',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HufQuizQn',
            fields=[
                ('quiz_qn_id', models.AutoField(primary_key=True, serialize=False)),
                ('correct_ans', models.IntegerField()),
                ('question_name', models.CharField(max_length=30)),
                ('score_per_qn', models.IntegerField()),
            ],
            options={
                'db_table': 'huf_quiz_qn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HufUser',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=12, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('user_password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'huf_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HufQuizOption',
            fields=[
                ('quiz_qn', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='loginapi.hufquizqn')),
                ('game_option', models.IntegerField()),
            ],
            options={
                'db_table': 'huf_quiz_option',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HufQuizResult',
            fields=[
                ('quizid', models.OneToOneField(db_column='quizid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='loginapi.hufquiz')),
                ('score_earned', models.IntegerField()),
                ('duration_taken', models.IntegerField()),
            ],
            options={
                'db_table': 'huf_quiz_result',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HufUserAns',
            fields=[
                ('userid', models.OneToOneField(db_column='userid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='loginapi.hufuser')),
                ('user_ans', models.IntegerField()),
            ],
            options={
                'db_table': 'huf_user_ans',
                'managed': False,
            },
        ),
    ]
