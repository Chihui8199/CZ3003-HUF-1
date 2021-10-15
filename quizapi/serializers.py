from rest_framework import serializers
from .models import HufQuiz, HufQuizOption, HufQuizQn, HufQuizResult


class HufQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = HufQuiz
        fields = ('quiz_id', 'game_id', 'quiz_duration', 'quiz_max_score', 'quiz_description', 'no_of_qn')


class HufQuizOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HufQuizOption
        fields = ('quiz_qn_id', 'option_id', 'option_description')


class HufQuizQnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HufQuizQn
        fields = ('quiz_qn_id', 'quiz_id', 'correct_ans', 'question_name', 'score_per_qn')


class HufQuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = HufQuizResult
        fields = ('quiz_id', 'user_id', 'score_earned', 'duration_taken')


# class HufUserAnsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HufUserAns
#         fields = ('username', 'quiz_qn_id', 'user_ans')
