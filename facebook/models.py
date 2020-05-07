from django.db import models

# django의 모델링
#models.py는 데이터베이스 즉 모델에 대한 설명서 역할을 한다.
#max_length <- 글자수, 나머지 앞 부분 <- 필드의 형태

#PAGE 리스트를 보여준다
class Page(models.Model):
    #페이지 관리자 master
    master      = models.CharField(max_length=120)
    #페이지 명
    name        = models.CharField(max_length=120)
    text        = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    category    = models.CharField(max_length=120,default='전체')

# 모델의 기능과 상관 없이 관리자 페이지에서 표시할 이름 선택
    def __str__(self):
        return self.name

#작성한 글 보여주는 모델
class Article(models.Model):
    author      = models.CharField(max_length=120)
    title       = models.CharField(max_length=120)
    text        = models.TextField()
    password    = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)

#모델의 기능과 상관 없이 관리자 페이지에서 표시할 이름 선택
    def __str__(self):
        return self.title

class Comment(models.Model):
    #다른 모델과 관련있는 모델을 넣을 때 ForeignKey 타입 사용
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text