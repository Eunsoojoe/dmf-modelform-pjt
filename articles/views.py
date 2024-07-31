from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }

    return render(request, 'index.html', context)

def create(request):
    # 모든 경우의 수
    # GET : form을 만들어서 html 문서를 사용자에게 리턴 => 1~4번.
    # POST invalid data(데이터 검증에 실패한 경우)
    # POST valid data(데이터 검증에 성공한 경우) 

    # 기존
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터를 저장하는 기능
    
    # 5. POST 요청 (데이터가 잘못 들어온 경우)
    # 10. POST 요청 (데이터가 잘 들어온 경우)
    if request.method == 'POST':
        # 6. 사용자가 입력한 데이터X(request.POST)을 담아서 form 생성
        # 11. 사용자가 입력한 데이터O(request.POST)을 담아서 form 생성
        form = ArticleForm(request.POST)

        # 7. form 검증 실패
        # 12. form 검증 성공
        if form.is_valid():
            # 13. form을 저장
            form.save()         # '검증'하여 데이터를 '한꺼번에' 저장
            
            # 14. index 페이지로 redirect
            return redirect('articles:index')

            # article = Article()
            # article.title = title
            # article.save()
            
        # 사용자가 데이터를 잘못 넣은 경우
        # else:    
            # form = ArticleForm()

            # 너 게시물 그만 작성하고 index로 돌아갓 근데 사용자가 실수했을 수도 있잖아?
            # return redirect('articles:index')  

            # context = {
            #     'form':form,
            # }
            # return render(request, 'create.html', context)

    # 1. GET create/ => 빈 종이를 보여주는 기능
    else:
        # 2. 비어있는 form을 만들어서 
        form = ArticleForm()

    # 3. context dict에 비어있는 form을 담아서
    # 8. context dict에 검증에 실패한 form을 담아서 
    context = {
        'form' : form,
    }

    # 4. create.html을 랜더링
    # 9. create.html을 랜더링
    return render(request, 'create.html', context)
    
    # forms.py에서 만든 ArticleForm 인스턴스화
    