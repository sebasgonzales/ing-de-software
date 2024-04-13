from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField se usa como un campo de texto con un número limitado de caracteres
    pub_date = models.DateTimeField('date published') # DateTimeField se usa para la fecha y hora de la publicación

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey se usa para definir una relación de muchos a uno con el modelo Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # IntegerField se usa para almacenar un entero de votos para cada elección y se define un valor predeterminado de 0 para los votos