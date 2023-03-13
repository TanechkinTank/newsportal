from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin


class AuthorAdmin(TranslationAdmin):
    model = Author


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


class PostCategoryAdmin(TranslationAdmin):
    model = PostCategory


class CommentAdmin(TranslationAdmin):
    model = Comment


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

