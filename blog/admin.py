from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','count_text']
    list_display_links = ['title']

    def count_text(self,obj):
        return '{}글자'.format(len(obj.text))
    count_text.short_description = '글내용 글자수'

admin.site.register(Post,PostAdmin)
#admin.site.register(Post)