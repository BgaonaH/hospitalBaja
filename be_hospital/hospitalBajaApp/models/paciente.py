from unittest.util import _MAX_LENGTH
from django.db import models
from .usuario import Usuario
from .medico import Medico


class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)
    f_cardiaca=models.IntegerField()
    temperatura=models.IntegerField()
    p_arterial=models.CharField(max_length=30)
    oximetria=models.IntegerField()