from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline): # StackedInline --> TabularInline
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)