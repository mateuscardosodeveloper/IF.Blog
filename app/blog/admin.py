from django.contrib import admin

from .models import BlogPost
from searches.models import SearchQuery
from comment.models import Comment


admin.site.register(BlogPost)
admin.site.register(SearchQuery)
admin.site.register(Comment)
