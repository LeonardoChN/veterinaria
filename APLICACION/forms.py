from django import forms
from APLICACION.models import tipo_at,tipo_m,raza, funcionarios,mascota,clientes , cita


class formTipoat (forms.ModelForm):
    class Meta:
        model = tipo_at
        fields = '__all__'

class formTipom (forms.ModelForm):
    class Meta:
        model = tipo_m
        fields = '__all__'

class formRaza (forms.ModelForm):
    class Meta:
        model = raza
        fields = '__all__'


## separacion
class formFunc (forms.ModelForm):
    class Meta:
        model = funcionarios
        fields = '__all__'

class formMasc(forms.ModelForm):
    class Meta:
        model = mascota
        fields = '__all__'

class formCliente(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'


##separacion 
class formCita(forms.ModelForm):
    class Meta:
        model = cita
        fields = '__all__'
