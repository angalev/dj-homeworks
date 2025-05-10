from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Article, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
        if count == 0:
            raise ValueError('Ошибка. Выберите основной тег')
        elif count > 1:
            raise ValueError('Основным может быть только один тег')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Scope)
class ObjectAdmin(admin.ModelAdmin):
    pass