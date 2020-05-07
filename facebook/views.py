from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

# Create your views here.
def play(request):
    return render(request, 'play.html')

def play2(request):
    mimi='미미'
    list = ['01.시작하기', '02.더 나아가기', '03.거의 끝이야!']
    return render(request, 'play2.html', {'name': mimi, 'list':list})

def profile(request):
    return render(request,'profile.html')

def newsfeed(request):
    #ORM을 이용해 쿼리셋을 가져오는 명령어 모든 Article 객체의 쿼리셋을 가져와 할당
    articles = Article.objects.all()
    return render(request,'newsfeed.html',{'articles':articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password']
        )
        return redirect(f'/feed/{article.pk}')

    return render(request, 'detail_feed.html', {'feed': article})

def pages(request):
    pages=Page.objects.all()
    return render(request, 'page_list.html', {'pages':pages})

#이제는 관리자 말고 유저들이 작성할 수 있도록 만드는 피드입니다.
#폼이 전송되었을 때만, 쓸 수 있도록
def new_feed(request):
    #게시 버튼을 누르면 POST가 활성화된다.
    #장고에서는 request.method가 POST가 활성화됩니다.
    if request.method == 'POST':
        #빈 내용이 있으면 게시할 수 없도록 하는 조건문
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            #Article 모델에 새로운 글을 create 하라는 명령
            #create 됨과 동시에 new_article에 새롭게 쓰여진 글의 정보 자동 등록
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )
            #새글 등록 끝 <- redirect 기능은 특정 페이지로 이동하게끔 하는 것.
            #new_article.pk는 글의 번호 자료를 따옴표 안에 넣으려면 맨앞에 f를 붙이고 {}안에 넣기
            return redirect(f'/feed/{ new_article.pk }')
    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/newsfeed/')  # newsfeed로 이동하기
        else:
            return redirect('/fail/')

    return render(request, 'remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')
        else:
            return redirect('/fail/')

    return render(request, 'edit_feed.html', {'feed': article})

def fail(request):
    return render(request, 'fail.html')