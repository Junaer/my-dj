from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInLineFormset(BaseInlineFormSet):
   def clean(self):
       count = 0
       for form in self.forms:
           if not form.cleaned_data:
               continue
           if form.cleaned_data.get('is_main', False):
               count += 1
       if count > 1:
           raise ValidationError('Слишком много главных тегов')
       if count == 0:
           raise ValidationError('Укажите главный тег')
       return super().clean()

class ScopeInline(admin.TabularInline):
   model = Scope
   formset = ScopeInLineFormset
   extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   pass