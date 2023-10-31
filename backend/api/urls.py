from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ListarAlunos.as_view(),name='listar'),
    path('cadastro', views.CadastrarAluno.as_view(),name='cadastro'),
    path('aluno/<int:pk>', views.ListaAluno.as_view(), name='lista'),
    path('aluno/<int:pk>/atualizar', views.UpdateAluno.as_view(), name='update'),
    path('aluno/<int:pk>/deletar', views.DeleteAluno.as_view(), name='deletar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)