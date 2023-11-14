from django import forms
from django.core.exceptions import ValidationError 
from datetime import datetime


class MyForm(forms.Form):
    start_date = forms.DateField(
        label='start_date',
        input_formats=['%d/%m/%Y'],
        help_text="Formato: dd/mm/YYYY" #help_text, nos permite mostrar un comentario
    )
    end_date = forms.DateField(
        label='end_date',
        input_formats=['%d/%m/%Y'],
        help_text="Formato: dd/mm/YYYY"
    )
    days_of_week = forms.MultipleChoiceField(
        choices=[
            ('monday', 'Lunes'),
            ('tuesday', 'Martes'),
            ('wednesday', 'Miércoles'),
            ('thursday', 'Jueves'),
            ('friday', 'Viernes'),
            ('saturday', 'Sábado'),
            ('sunday', 'Domingo'),
        ],
        label="days_of_week",
        widget=forms.CheckboxSelectMultiple,
        help_text="Selecciona uno o varios días de la semana."
    )
    email = forms.EmailField(
        label="email",
        help_text="Correo electrónico"
    )
    
    
    def clean(self):
        cleaned_data=super().clean()
        start_date=cleaned_data.get("start_date")
        end_date=cleaned_data.get("end_date")
      
      

        if start_date and end_date and start_date > end_date:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")

        
        return cleaned_data
    
    
    def clean_days_of_week(self):
        days_of_week = self.cleaned_data["days_of_week"]
        
        if len(days_of_week) < 1:
            raise ValidationError(
                "No ha elegido ningun dia de la semana"
                )
            
        if len(days_of_week) > 3:
            raise ValidationError(
                "Ha elegido mas de 3 dias de la semana"
                )
        
        return days_of_week
    
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if not email.lower().endswith("@iesmartinezm.es"):
            raise ValidationError("El correo electrónico debe terminar con @iesmartinezm.es")
        
        return email

