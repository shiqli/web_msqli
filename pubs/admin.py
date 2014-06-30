from django.contrib import admin
from pubs.models import Publisher, Author, Book, Journal, Publication, Keyword,AuthorSequencing

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(Publication)
admin.site.register(Journal)
admin.site.register(Keyword)
admin.site.register(AuthorSequencing)
# Register your models here.
