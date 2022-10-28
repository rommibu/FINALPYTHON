from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.utils import timezone





class Seccional(models.Model):
    nombre=models.CharField(max_length=50)
    numseccional:models.IntegerField() 
    
    def __str__(self):
        return self.nombre 

class Asociado(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.FloatField()
    extranjero=models.BooleanField()
    mail=models.EmailField()
    barrio=models.CharField(max_length=60)
    
    def __str__(self):
        return self.apellido 
    

class Caracteristicas(models.Model):
    asociado=models.CharField(max_length=60)
    codigo=models.IntegerField()
    fecha_creacion=models.DateField()
    intereses=models.TextField(max_length=600) 
    
    def __str__(self):
        return self.asociado


class Entrada(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=800)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre 

class Comentario(models.Model):
    nombre=models.CharField(max_length=60)
    comentario = models.TextField(max_length=500)
    
    def __str__(self):
        return self.nombre


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def following(self):
        user_ids=Relationship.objects.filter(from_user=self.user)\
                            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def followers(self):
        user_ids=Relationship.objects.filter(to_user=self.user)\
                            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'



class Autos(models.Model):
    nombre = models.CharField(max_length=30)
    
    escuderias= [
        ('Ferrari','Ferrari'),
        ('Mercedes','Mercedes'),
        ('Alpine','Alpine'),
        ('Haas','Haas'),
        ('Alfa Romeo','Alfa Romeo'),
        ('Aston Martin','Aston Martin'),
        ('Alphatauri','Alphatauri'),
        ('Williams','Williams'),
        ('Red Bull','Red Bull'),
        ('Mclaren','Mclaren'),
        
    ]
    
    escuderias = models.CharField(max_length=30,choices=escuderias,default='Ferrari')
    piloto = models.IntegerField()
    
    def __str__(self):
        return self.nombre 
    
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)

class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='relationship', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.from_user} to {self.to_user}'
    
    class Meta:
        indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		] 



