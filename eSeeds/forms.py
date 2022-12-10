from django.forms import ModelForm
from .models import * 

class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente 
        fields = '__all__'

class atencionClienteForm(ModelForm):
    
    class Meta:
        model = atencionCliente 
        fields = '__all__'