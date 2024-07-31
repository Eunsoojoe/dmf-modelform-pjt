from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta():
        # Article과 어울리는 html코드를 자동으로 생성
        model = Article
        fields = '__all__'