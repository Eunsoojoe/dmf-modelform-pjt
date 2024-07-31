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
    # 기존
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터를 저장하는 기능
    

    # POST create/ => 사용자가 입력한 데이터를 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()         # '검증'하여 데이터를 '한꺼번에' 저장
            return redirect('articles:index')

            # article = Article()
            # article.title = title
            # article.save()
            
        # 사용자가 데이터를 잘못 넣은 경우
        else:    
            # form = ArticleForm()
            context = {
                'form':form,
            }

            # 너 게시물 그만 작성하고 index로 돌아갓 근데 사용자가 실수했을 수도 있잖아?
            # return redirect('articles:index')    

            return render(request, 'create.html', context)

    # GET create/ => 빈 종이를 보여주는 기능
    else:
        
        form = ArticleForm()

        context = {
            'form' : form,
        }

        return render(request, 'create.html', context)
    
    # forms.py에서 만든 ArticleForm 인스턴스화
    