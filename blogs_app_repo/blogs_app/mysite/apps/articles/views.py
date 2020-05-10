from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy			# USE VIRTUAL ENVIRONMENT! myvenv\Scripts\activate
											
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


'''def home_page(request):
	#last_articles_list = Article.objects.order_by('-pub_date') # view 10 last articles
	context = {
		'last_articles_list': Article.objects.order_by('-pub_date'), # view 10 last articles
	}
	return render(request, 'articles/homepage.html', context)'''

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/homepage.html'
    context_object_name = 'articles'
    ordering = ['-pub_date']
    paginate_by = 3


class UserArticlesListView(ListView):
    model = Article
    template_name = 'articles/user_posts.html'
    context_object_name = 'user_articles'
    ordering = ['-pub_date']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(
        User,
        username=self.kwargs.get('username'))

        return Article.objects.filter(author_article=user).order_by('-pub_date')


def about(request):
	return render(request, 'articles/about.html')


@login_required
def detail(request, slug):
    #template_name = 'detail.html'
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

'''def by_rubric(request, rubric_id):
    rs = Article.objects.filter(rubric=rubric_id)
    current_rubric = Rubric.objects.get(pk=rubric_id)

    context = {
    'rs': rs,
    'current_rubric':current_rubric
    }

    return render(request, 'articles/by_rubric.html', context)'''


class RubricArticlesListView(ListView):
    model = Rubric
    template_name = 'articles/by_rubric.html'
    context_object_name = 'by_rubric'
    ordering = ['-pub_date']
    paginate_by = 3


    def get_queryset(self):
        by_rubric = get_object_or_404(
        Rubric,
        #rubric_name=self.kwargs.get('rubric_name'),
        rubric_slug=self.kwargs.get('rubric_slug'))

        return Article.objects.filter(rubric_id=by_rubric).order_by('-pub_date')


'''@login_required
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,
                                    request.FILES)

        if form.is_valid():
			# save article to db
            instanse = form.save(commit=False)
            instanse.author_article = request.user
            instanse.save()
            messages.success(request, 'You created an article!')
            return redirect('articles:articles_home')
    else:
	    form = forms.CreateArticle()
    return render(request, 'articles/article_form.html', {'form': form} )'''
    #return HttpResponseRedirect( reverse('articles:detail',
	#args = (slug.slug,)) )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['article_title', 'article_text', 'slug', 'rubric', 'image']
    '''success_url = reverse_lazy('detail',
                        kwargs={'slug': articles:slug},
                        current_app='articles   ')'''
    success_url = reverse_lazy('articles:articles_home')
        #return HttpResponseRedirect( reverse('articles:detail', args = (article.slug,)
    def form_valid(self, form):
        form.instance.author_article = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Article
	fields = ['article_title', 'article_text', 'rubric', 'image']

	def form_valid(self, form):
		form.instance.author_article = self.request.user
		return super().form_valid(form)


	def test_func(self):                   #checking user
		post = self.get_object()
		if self.request.user == post.author_article:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('articles:articles_home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author_article:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author_comment or self.request.user == post.author_article:
            return True
        return False


class MyCommentDeleteView(CommentDeleteView):
    
    def get_success_url(self):
        messages.error(self.request, 'You deleted a comment.')
        return reverse_lazy('articles:detail', kwargs={'slug': self.object.article.slug})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment_text']

    def get_success_url(self):
        messages.info(self.request, 'You updated a comment.')
        return reverse_lazy('articles:detail', kwargs={'slug': self.object.article.slug})

    def form_valid(self, form):
        form.instance.author_comment = self.request.user
        return super().form_valid(form)


    def test_func(self):                   #checking user
        post = self.get_object()
        if self.request.user == post.author_comment:
            return True
        return False
