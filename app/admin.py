from django.contrib import admin
from .models import Home, Profiles, About, AboutProfile, Skill, Achievement, Portfolio, ContactFormLog

# Inline admin for Profiles linked to Home
class ProfilesInline(admin.TabularInline):
    model = Profiles
    extra = 2

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated')
    inlines = [ProfilesInline]
    search_fields = ['name']
    ordering = ['-updated']


# Inline admin for AboutProfile linked to About
class AboutProfileInline(admin.TabularInline):
    model = AboutProfile
    extra = 2

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'career', 'updated')
    inlines = [AboutProfileInline]
    search_fields = ['career', 'heading']
    ordering = ['-updated']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'is_left')
    list_filter = ('is_left',)
    search_fields = ('name',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'icon_class', 'icon_color')
    list_filter = ('year',)
    search_fields = ('title', 'description')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'link')
    ordering = ['id']



@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    
    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]

    def has_add_permission(self, request, object = None):
        return False
    
    # Show to disable update permission
    def has_change_permission(self, request, object = None):
        return False
    
    #Show to disable delete permission
    def has_delete_permission(self, request, object = None):
        return False
