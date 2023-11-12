from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError 


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
        widget=forms.CheckboxSelectMultiple,
        help_text="Selecciona uno o varios días de la semana."
    )
    email = forms.EmailField(
        help_text="Correo electrónico"
    )
    
    def clean(self):
        cleaned_data=super().clean()
        start_date  =cleaned_data.get("start_date")
        end_date=cleaned_data.get("end_date")
      

        if end_date<start_date:
            raise ValidationError(
                "Ha introducido mal la fecha de inicio o fin"
                )
        
        return cleaned_data