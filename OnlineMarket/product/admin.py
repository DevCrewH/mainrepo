from django.contrib import admin
from .models import Review, Product, Rating

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "type", "posted_time"]
    list_filter = ["price", "type"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "review_date"]

class RatingAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "rate", "rated_at"]

admin.site.register(Review,ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)
