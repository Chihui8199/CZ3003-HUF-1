# Generated by Django 3.2.8 on 2021-10-17 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HufQuiz',
            fields=[
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('quiz_duration', models.IntegerField()),
                ('quiz_max_score', models.IntegerField()),
                ('quiz_description', models.CharField(blank=True, max_length=50, null=True)),
                ('no_of_qn', models.IntegerField()),
                ('game_id', models.ForeignKey(db_column='game_id', on_delete=django.db.models.deletion.CASCADE, to='gameapi.hufgame')),
            ],
        ),
        migrations.CreateModel(
            name='HufQuizQn',
            fields=[
                ('quiz_qn_id', models.AutoField(primary_key=True, serialize=False)),
                ('correct_ans', models.IntegerField()),
                ('question_name', models.CharField(max_length=30)),
                ('score_per_qn', models.IntegerField()),
                ('quiz_id', models.ForeignKey(db_column='quiz_id', on_delete=django.db.models.deletion.DO_NOTHING, to='quizapi.hufquiz')),
            ],
        ),
        migrations.CreateModel(
            name='HufQuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_earned', models.IntegerField()),
                ('duration_taken', models.IntegerField()),
                ('quiz_id', models.ForeignKey(db_column='quiz_id', on_delete=django.db.models.deletion.DO_NOTHING, to='quizapi.hufquiz')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('quiz_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='HufQuizOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.IntegerField()),
                ('option_description', models.CharField(blank=True, max_length=50, null=True)),
                ('quiz_qn_id', models.ForeignKey(db_column='quiz_qn_id', on_delete=django.db.models.deletion.DO_NOTHING, to='quizapi.hufquizqn')),
            ],
            options={
                'unique_together': {('quiz_qn_id', 'option_id')},
            },
        ),
    ]
