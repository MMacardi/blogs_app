from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy			# USE VIRTUAL ENVIRONMENT! blogs_venv\Scripts\activate
											
from django.views.generic import CreateView

from accounts.models import Profile

from .models import (
    Article,
    Rubric,
    Comment
    )

from django.contrib.auth.decorators import login_required

from . import forms

from accounts.forms import UserUpdateForm, ProfileUpdateForm

from django.contrib import messages

from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#from django import forms

#from emoji_picker.widgets import EmojiPickerTextInput, EmojiPickerTextarea


class ArticleListView(ListView):
    model = Article
    ordering = ['-pub_date']
    paginate_by = 3
    template_name = 'articles/homepage.html'
    context_object_name = 'articles'


class UserArticlesListView(ArticleListView, ListView):
    template_name = 'articles/user_posts.html'
    context_object_name = 'user_articles'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(
        User,
        username=self.kwargs.get('username'))

        return Article.objects.filter(author_article=user)#.order_by('-pub_date')


def about(request):
	return render(request, 'articles/about.html')


#@login_required
def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    last_comments_list = article.comment_set.order_by('-pub_date') # view 10 last comms
    new_comment = None
    image = article.image
    # Comment posted
    if request.method == 'POST':
        comment_form = forms.LeaveComment(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # get username
            new_comment.author_comment = request.user
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'You created a comment!')
            return HttpResponseRedirect( reverse('articles:detail', args = (article.slug,))
            ) # doing it on fly, set the comment to article

    else:
        comment_form = forms.LeaveComment()

    return render(request, 'articles/detail.html', {'article': article,
                                                    'last_comments_list': last_comments_list,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form,
                                                    'image': image})


# Rubrics Stuff

def list_rubrics(request):
	rubrics = Rubric.objects.all()
	return render(request, 'articles/list_rubrics.html', {
	'rubrics': rubrics
	})


class RubricArticlesListView(ListView):
    model = Rubric
    template_name = 'articles/by_rubric.html'
    context_object_name = 'by_rubric'
    ordering = ['-pub_date']
    paginate_by = 5

    def get_queryset(self):
        by_rubric = get_object_or_404(
        Rubric,
        #rubric_name=self.kwargs.get('rubric_name'),
        rubric_slug=self.kwargs.get('rubric_slug'))

        return Article.objects.filter(rubric_id=by_rubric).order_by('-pub_date')


class Post(LoginRequiredMixin):
    model = Article

    def form_valid(self, form):
        form.instance.author_article = self.request.user
        return super().form_valid(form)

    def test_func(self):                   #checking user
        post = self.get_object()
        if self.request.user == post.author_article:
            return True
        return False

class PostCreateView(Post, CreateView):
    fields = ['article_title', 'article_text', 'slug', 'rubric', 'image']

    def get_success_url(self):
        messages.success(self.request, 'You created an article')
        return reverse_lazy('articles:detail', kwargs={'slug': self.object.slug})


class PostUpdateView(Post, UserPassesTestMixin, UpdateView):
	fields = ['article_title', 'article_text', 'rubric', 'image']


class PostDeleteView(Post, UserPassesTestMixin, DeleteView):
    success_url = reverse_lazy('articles:articles_home')


class Comment_view(LoginRequiredMixin, UserPassesTestMixin):
    model = Comment

    def test_func(self):                   #checking user
        post = self.get_object()
        if self.request.user == post.author_comment:
            return True
        return False

class Comment_delete(Comment_view, DeleteView):

    def get_success_url(self):
        messages.error(self.request, 'You deleted a comment.')
        return reverse_lazy('articles:detail', kwargs={'slug': self.object.article.slug})


class Comment_update(Comment_view, UpdateView):
    fields = ['comment_text']

    def get_success_url(self):
        messages.info(self.request, 'You updated a comment.')
        return reverse_lazy('articles:detail', kwargs={'slug': self.object.article.slug})

    def form_valid(self, form):
        form.instance.author_comment = self.request.user
        return super().form_valid(form)
