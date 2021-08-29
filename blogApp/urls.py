from os import name
from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/comment/', views.addCommentsToPost, name='add_comments_to_post'),
    path('comment/approve/', views.commentsApprove, name='comment_approve'),
    path('comment/remove/', views.commentRemove, name='comment_remove'),
    path('post/publish', views.postPublish, name='post_publish')
]
