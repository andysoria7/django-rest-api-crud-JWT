from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    completed = models.BooleanField(default=False, verbose_name="Completada")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        
    
    
