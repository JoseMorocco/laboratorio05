from django.db import models

# Modelo usuario
# Registrar en admin.py

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    es_profesional = models.BooleanField(default=False)
    biografia = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=100, blank=True)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
# Match

class Match(models.Model):
    usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='matchs_enviados')
    usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='matchs_recibidos')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Match entre {self.usuario1} y {self.usuario2}'
    
# Modelo Mensaje
class Mensaje(models.Model):
    emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.emisor} a mensajeado a {self.receptor}'



class Cita(models.Model):
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()

    def _str_(self):
        return f"Cita el {self.fecha} en {self.ubicacion}"

class Cita_usuarios(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='usuarios')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas')

    def _str_(self):
        return f"Usuario {self.usuario} para la cita {self.cita}"

class Reseña(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reseñas_escritas')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reseñas_recibidas')
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fecha = models.DateTimeField()

    def _str_(self):
        return f"Reseña de {self.autor} a {self.receptor} - Calificación: {self.calificacion}"
