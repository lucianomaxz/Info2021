from django.contrib import admin
from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, AddCommentView,enviarAdmin,bloquearUsuarios,listarUsers,search

urlpatterns = [
    #path('', views.home, name="home"),
    path('admin/', admin.site.urls,name='admins'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('enviarAdmin/', enviarAdmin, name = 'enviarAdmin'),
    path('bloquearUsuarios/',bloquearUsuarios,name = 'bloquearUsuarios'),
    path('listarUsers/',listarUsers,name = 'listarUsers'),
    path('search/',search,name = 'search'),
]
