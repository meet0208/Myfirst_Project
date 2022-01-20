from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create', views.create, name='create'),
    path('save', views.save, name='save'),
    path('<int:question_id>/options', views.options, name='options'),
    path('<int:question_id>/choice', views.choice, name='choice'),
   
    
]
