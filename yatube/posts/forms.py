from django.contrib.auth.forms import *
from .models import Post

class PostForm(Post.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
