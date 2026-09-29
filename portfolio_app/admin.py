from django.contrib import admin
from .models import Profile, Education, SkillCategory, Skill, Project, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'degree_badge', 'email', 'phone')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'duration', 'score_value', 'order')
    list_editable = ('order',)
    list_filter = ('category',)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 2

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name', 'order')
    list_editable = ('order',)
    inlines = [SkillInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'date_label', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'description', 'tech_stack')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
