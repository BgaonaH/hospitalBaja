from dataclasses import field
from rest_framework import serializers
from hospitalBajaApp.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=('usuario','medico')