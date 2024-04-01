from django.contrib import admin
from .models import Review, Post, Rating

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "type", "posted_time"]
    list_filter = ["price", "type"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "review", "review_date"]

class RatingAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "rate", "rated_at"]

admin.site.register(Review,ReviewAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Rating, RatingAdmin)
