from django.contrib import admin
from polls.models import Poll, Question, Choice


# Register your models here.
class PollsAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['poll', 'question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes']



admin.site.register(Poll, PollsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
