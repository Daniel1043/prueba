
import os
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ImageUploadForm, ImageDeleteForm

def bienvenido(request):
    return render(request, 'imagen/index.html', {}) 



def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            
            # Verifica la extensión y el tamaño antes de guardar la imagen
            if image.name.split('.')[-1].lower() not in ['jpg', 'png']:
                return render(request, 'upload.html', {'form': form, 'error': 'La extensión de la imagen no es válida.'})
            
            if image.size > 50000:  # 50KB
                return render(request, 'upload.html', {'form': form, 'error': 'La imagen es demasiado grande (máximo 50KB).'})

            # Guarda la imagen en un directorio específico (puedes cambiar 'images' a tu preferencia)
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', image.name)
            with open(image_path, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            return redirect('image_gallery')
    else:
        form = ImageUploadForm()

    return render(request, 'imagen/subir.html', {'form': form})



def image_gallery(request):
    # Obtén la lista de archivos en el directorio de imágenes
    image_dir = os.path.join(settings.MEDIA_ROOT, 'images')
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    return render(request, 'imagen/galeria.html', {'images': images})

def delete_image(request):
    if request.method == 'POST':
        form = ImageDeleteForm(request.POST)
        if form.is_valid():
            image_id = form.cleaned_data['image_id'] #sirve para borrar cleaned_data
            # Aquí puedes agregar la lógica para eliminar la imagen si lo deseas
            return redirect('image_gallery')
    else:
        form = ImageDeleteForm()

    return render(request, 'imagen/delete.html', {'form': form})
# Create your views here.
