from django.contrib import admin

from .models import Question

# Register your models here.

admin.site.register(Question) # Para hacer que nuestro modelo sea visible en la página de administración, tenemos que registrar el modelo con admin.site.register(Question)
