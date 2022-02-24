from django.contrib import admin
from filter_history.models import User, Keyword, Result, History

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip_address']

class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'word']

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'search_result', 'keyword']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'date', 'user', 'keyword']

admin.site.register(User, UserAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(History, HistoryAdmin)