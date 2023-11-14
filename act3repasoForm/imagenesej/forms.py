from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        # Realiza tus validaciones aquí
        return image

class ImageDeleteForm(forms.Form):
    image_id = forms.IntegerField(widget=forms.HiddenInput())
    