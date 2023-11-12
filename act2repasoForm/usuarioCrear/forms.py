from django import forms
from django.core.exceptions import ValidationError 
from datetime import datetime, timedelta
from django.utils import timezone

class MyForm(forms.Form):
    nombre = forms.CharField( label='nombre', max_length=30, required= True, help_text="Introduzca su nombre")
    
    contraseña = forms.CharField(label='contraseña', widget=forms.PasswordInput, max_length=30, required= True, help_text="Introduzca su contraseña")
     
    fecha_acceso = forms.DateTimeField(label='fecha_acceso', initial=datetime.now, widget=forms.HiddenInput, required= False)
      
    def clean(self):
        cleaned_data=super().clean()
        nombre  =cleaned_data.get("nombre")
        contraseña=cleaned_data.get("contraseña")
        fecha_acceso=cleaned_data.get("fecha_acceso")
        special_characters = "!@#$%^&*()-_=+[]|;:'\",.<>/?"

        if nombre==contraseña:
            raise ValidationError("La contraseña y el nombre no pueden ser el mismo" )
        
        if len(contraseña) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")

         
        if not any(char in special_characters for char in contraseña):
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")

        if not any(char.isdigit() for char in contraseña):
            raise ValidationError("La contraseña debe contener al menos un número.")

        # Verificar si hay al menos una letra minúscula
        if not any(char.islower() for char in contraseña):
            raise ValidationError("La contraseña debe contener al menos una letra minúscula.")

        # Verificar si hay al menos una letra mayúscula
        if not any(char.isupper() for char in contraseña):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        
        if fecha_acceso:
            ahora = datetime.now()
            diferencia_tiempo = ahora - fecha_acceso

            if diferencia_tiempo.total_seconds() > 120:  # 120 segundos = 2 minutos
                # Reiniciar los datos y cambiar la fecha oculta
               
                cleaned_data['fecha_acceso'] = ahora
                cleaned_data['contraseña'] = ''
                cleaned_data['usuario'] = ''
        
        return cleaned_data
