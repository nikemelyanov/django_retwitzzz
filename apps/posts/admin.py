from django.contrib import admin

from apps.posts.models import Post, PostComment

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_timestamp')
    fields = ('user', 'title', 'body')
    search_fields = ('title',)
    
@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_timestamp')
    fields = ('user', 'post', 'body')
    search_fields = ('body',)