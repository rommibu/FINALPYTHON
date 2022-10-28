from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path ('', inicio, name='inicio'),
    path ('seccional/', seccional, name='seccional'),
    path ('asociado/', asociado, name='asociado'),
    path ('caracteristicas/', caracteristicas, name='caracteristicas'),
    path ('conocenos/', conocenos, name='conocenos'),
    path('leerAsociado/',  leerAsociado, name='leerAsociado'),
    path('leerSeccional/',  leerSeccional, name='leerSeccional'),
    path('leerCaracteristicas/',  leerCaracteristicas, name='leerCaracteristicas'),
    path('eliminarAsociado/<id>', eliminarAsociado, name='eliminarAsociado'),
    path('editarAsociado/<id>', editarAsociado, name='editarAsociado'),
    path('busquedaAsociado/', busquedaAsociado, name='busquedaAsociado'),
    path('busquedaescu/',busquedaescu,name='busquedaescu'),
    path('Buscar/',Buscar,name='Buscar'),
    path('escuderia/', escuderia, name='Eventos'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('editarProfile/', editarProfile, name='editarProfile'),
    path('seccional/<pk>', SeccionalDetalle.as_view(), name='seccional_detalle'),
    
    path('register/', views.register, name='register'),   
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('login/', LoginView.as_view(template_name='AppParadigma/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='AppParadigma/logout.html'), name='logout'),
	path('post/', views.post, name='post'),
	path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)