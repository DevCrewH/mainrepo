from django.contrib import admin
from .models import Review, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "type"]
    list_filter = ["price", "type"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "review", "review_date"]

admin.site.register(Review,ReviewAdmin)
admin.site.register(Post, PostAdmin)
