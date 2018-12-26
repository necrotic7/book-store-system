from django.contrib import admin

from .models import Author, Publish, Classification, Tag, Book

admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(Classification)
admin.site.register(Tag)
admin.site.register(Book)
