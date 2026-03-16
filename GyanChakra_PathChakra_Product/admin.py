from django.contrib import admin
from .models import PathChakraModel, PathChakraBookChapterModels, PathChakraUserAssignModel
# Register your models here.

class PathChakraModelAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author_name', 'status', 'start_date', 'end_date')
    search_fields = ('book_name', 'author_name')
    list_filter = ('status',)

class PathChakraBookChapterModelsAdmin(admin.ModelAdmin):
    list_display = [chapter.name for chapter in PathChakraBookChapterModels._meta.fields if chapter.name ]
    search_fields = ('chapter_name', 'path_chakra__book_name')

class PathChakraUserAssignModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PathChakraUserAssignModel._meta.fields]
    search_fields = ('user__username', 'path_chakra__book_name')

admin.site.register(PathChakraModel, PathChakraModelAdmin)
admin.site.register(PathChakraBookChapterModels, PathChakraBookChapterModelsAdmin)
admin.site.register(PathChakraUserAssignModel, PathChakraUserAssignModelAdmin)