import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


class Article(models.Model):
    article_title = models.CharField('title of article', max_length = 200)
    article_text = models.TextField('text of article')
    slug = models.SlugField(unique = True)
    author_article = models.ForeignKey(User, on_delete=models.CASCADE)
    rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, blank=True)
    pub_date = models.DateTimeField('date of publication', auto_now_add = True)
    image = models.ImageField('image', blank=True, upload_to='articles_images')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

    def get_absolute_url(self):
        return reverse('articles:detail', args=[self.slug])

    '''class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'''

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField('comment text', max_length = 250)
    pub_date = models.DateTimeField('date of publication', auto_now_add = True)

    '''def __str__(self):
        return self.author_name'''


    '''class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'''


class Rubric(models.Model):
    rubric_name = models.CharField(max_length=50, unique=True)
    rubric_slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.rubric_name
