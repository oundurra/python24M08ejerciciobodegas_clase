from django.db import models

# Create your models here.
class TipoBodega(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    metros = models.IntegerField()
    quimicos = models.BooleanField()
    organicos = models.BooleanField()
    hermetico = models.BooleanField()
    precio = models.IntegerField()

    def __str__(self):
        return self.tipo

class Bodega(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    tipo_bodega = models.ForeignKey(TipoBodega, models.DO_NOTHING)

    def __str__(self):
        return self.codigo

class User(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'auth_user'

class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=45)
    cuerpo = models.TextField()
    imagen_url = models.CharField(max_length=255)
    users = models.ManyToManyField(User,related_name='noticias', blank=True)