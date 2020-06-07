from django.contrib import admin

from session.models.session import Session
from session.models.section import Section
from session.models.item import Item
from session.models.choice import Choice
from session.models.verse import Verse
from model_clone import CloneModelAdmin

class VerseInline(admin.TabularInline):
    model = Verse

class SessionAdmin(admin.ModelAdmin):
    list_display = ('id_session', 'name', 'order', 'status',)
    list_filter = ('status',)


class SectionAdmin(CloneModelAdmin):
    list_display = ('id_section', 'name', 'order', 'status', 'session')
    list_filter = ('status', 'session')



class ItemAdmin(CloneModelAdmin):
    list_display = ('id_item', 'name', 'order', 'status', 'section')
    list_filter = ('status', 'section__session')
    # Enables/Disables the Duplicate action in the List view (Defaults to True)
    include_duplicate_action = True
    # Enables/Disables the Duplicate action in the Change view (Defaults to True)
    include_duplicate_object_link = True

    #inlines = (VerseInline,)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id_choice', 'name', 'order', 'status', 'item')

class VerseAdmin(admin.ModelAdmin):
    list_display = ('id_verse', 'book','chapter','verse','content')
    list_per_page = 15

admin.site.register(Session, SessionAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Verse,VerseAdmin)
admin.site.register(Choice,ChoiceAdmin)

