#Criando meu proprio formulário para adicionar posts no site

#Importamos o módulo do formulario django
from django import forms
#Importamos o modelo post
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)