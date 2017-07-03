from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'created_by')
    list_filter = ('created_by',)
    fieldsets = (
      ('Post info', {
          'fields': ('title', 'content', 'created_date', 'created_by', ('tags', 'views_total'))
      }),
   )

admin.site.register(Post, PostAdmin)
