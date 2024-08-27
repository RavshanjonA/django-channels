from django.contrib import admin

from chat.models import Room, Message


@admin.register(Room)
class RoomViewAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'body')
    date_hierarchy = 'date'
