from django.shortcuts import render, redirect
from .forms import MyForm

def welcome(request):
    return render(request, 'datos\index.html', {})


def success_page(request):
    return render(request, 'datos\exito.html')

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Realizar acciones adicionales con los datos del formulario
            return redirect('success_page')  # Redirige a una página de éxito
    else:
        form = MyForm()

    return render(request, 'datos\index.html', {'form': form})

