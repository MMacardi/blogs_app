from django import forms
from . import models

'''class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['article_title', 'article_text', 'slug', 'rubric', 'image']
'''

class LeaveComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment_text']
        # class Media:
        #     js = ('js/enter.js', )
