from django.contrib import admin
from .models import HufQuiz

# class HufQuizAdmin(admin.ModelAdmin):
#   list = ('quizid','gameid','quiz_duration','quiz_max_score','quiz_description','no_of_qn','total_no_qn')

admin.site.register(HufQuiz)
