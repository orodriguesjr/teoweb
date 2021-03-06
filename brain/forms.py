from django.forms import ModelForm

from .models import Clinica
from .models import Admin
from .models import Paciente
from .models import Profissional

class Clinica_Form(ModelForm):
    class Meta:
        model = Clinica
        fields = [
            'cnpj',
            'nome',
            'endereco',
            'contato',
        ]


class Admin_Form(ModelForm):
    class Meta:
        model = Admin
        fields = [
            'cpf',
            'nome',
            'contato',
            'cnpj_clinica',
        ]


class Paciente_Form(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cpf',
            'nome',
            'historico',
        ]


class Profissional_Form(ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'cpf',
            'nome',
            'contato',
            'especialidade',
            'cnpj_clinica',
        ]
