from django.contrib import admin
from .models import Article, Comment, Rubric


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'author_article', 'pub_date', 'rubric',)
    list_display_links = ('article_title',)
    search_fields = ('author_article__username',)
    readonly_fields = ('pub_date',)

    '''filter_horizontal = ()
    list_filter = ()
    fieldsets = ()'''
admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_comment', 'comment_text', 'pub_date',)
    list_display_links = ('author_comment',)
    search_fields = ('author_comment', 'comment_text',)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Rubric)
