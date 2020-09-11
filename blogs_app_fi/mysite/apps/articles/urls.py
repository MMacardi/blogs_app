from django.urls import path
from . import views
from .views import (
    PostUpdateView,
    PostDeleteView,
    ArticleListView,
    UserArticlesListView,
    RubricArticlesListView,
    Comment_delete, 
    Comment_update,
    PostCreateView,)
    #MyCommentDeleteView)


app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_home'), #views.home_page
    path('user/<str:username>/', UserArticlesListView.as_view(), name='user_articles'), #views.home_page and accounts_views.profile
    path('about/', views.about, name = 'articles_about'),
    path('rubrics/', views.list_rubrics, name='list_rubrics'),
    path('rubrics/<slug:rubric_slug>/', RubricArticlesListView.as_view(), name='by_rubric'),
    path('articles/<slug:slug>/', views.detail, name='detail'),
    #path('articles/<slug:slug>/update', views.update_article, name='update_article'),
    path('articles/<slug:slug>/update/', PostUpdateView.as_view(), name='article_update'),
    path('articles/<slug:slug>/delete/', PostDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>/comment_delete/', Comment_delete.as_view(), name='comment_delete'),
    path('articles/<int:pk>/comment_update/', Comment_update.as_view(), name='comment_update'),
    #path('articles/<slug:slug>/leave_comment', views.leave_comment, name='leave_comment'),
    path('create_article/', PostCreateView.as_view(), name='create_article'),
    #path('create_article/', views.create_article, name='create_article'),


]






































#{% for rubric in rubrics %}
#<menu>
#<li><a href="{% url 'by_rubric' rubric.pk %}">{{Rubric.name_of_rubric}}</a></li>
#</menu>
#{% endfor %}

#{% endblock %}
