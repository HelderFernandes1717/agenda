from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Para não fazer uma tabela de usuárui, estou usando os usuário do django

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    ## no caso aqui não seria necesspari apagar todos os evento
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    ## Evita aparece  na tela do admin objeto
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')


## python manage.py makemigration core ou depois
## python manage.py makemigrations core 0001 que é o nome do migration
## python manage.py sqlmigrate core 0001
## python manage.py migrate core 0001
## depois tem que ir no arquivo admim:
##    admin.site.registro

## adicionar o core nos settings


