from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ListaRelatorios', views.relatorioslist, name='relatorioslist'),
    path('ListaRelatorios/<int:id>/', views.edit, name='edit'),
    path('ListagemRelatorios/<int:id>/', views.edit, name='edit'),
    path('CadastrarRelatorio', views.post, name='post'),

]