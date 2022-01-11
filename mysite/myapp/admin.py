from django.contrib import admin

from myapp.models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    # Dit is om op het formulier van een `Question` direct een of meerdere `Answer` instanties aan te maken.
    fields = ["label"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswerInline,)
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # Je kunt hier van alles definieren, maar is niet verplicht, vandaar de pass.
    pass
