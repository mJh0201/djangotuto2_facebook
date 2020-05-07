from django.contrib import admin
from .models import Page
from .models import Article
from .models import Comment

# 관리자 페이지에서 만든 모델을 보기 위해 모델 등록,,
admin.site.register(Page)
admin.site.register(Article)
admin.site.register(Comment)