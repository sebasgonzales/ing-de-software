import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField se usa como un campo de texto con un número limitado de caracteres

    pub_date = models.DateTimeField('date published') # DateTimeField se usa para la fecha y hora de la publicación

    def __str__(self): # __str__() es un método que devuelve un valor legible para humanos cuando se llama a un objeto Question
        return self.question_text 

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey se usa para definir una relación de muchos a uno con el modelo Question

    choice_text = models.CharField(max_length=200)

    votes = models.IntegerField(default=0) # IntegerField se usa para almacenar un entero de votos para cada elección y se define un valor predeterminado de 0 para los votos

    def __str__(self):
        return self.choice_text