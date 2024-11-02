from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'rating', 'timestamp')
    list_filter = ('rating', 'timestamp')
    search_fields = ('user__username', 'message')