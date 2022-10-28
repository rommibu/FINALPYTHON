from django.contrib import admin
from .models import *
from AppParadigma.models import Entrada, Comentario
from .models import Post, Profile, Relationship

admin.site.register(Asociado)
admin.site.register(Caracteristicas)
admin.site.register(Seccional)
admin.site.register(Entrada)
admin.site.register(Comentario)
admin.site.register(Autos)
admin.site.register(Avatar)

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)

