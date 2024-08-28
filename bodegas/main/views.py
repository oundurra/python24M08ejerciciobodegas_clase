from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login
from django.template import Context
from .models import *
from .forms import *
from .services import *

# Create your views here.
def index(request):
    noticias = getLikesByUser(request.user.id)

    return render(request, 'index.html', {"noticias":noticias})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to a homepage or another page after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def add_like(request, user_id,  noticia_id):
    addLike(user_id, noticia_id)
    return redirect('home')   

def remove_like(request, user_id,  noticia_id):
    removeLike(user_id, noticia_id)
    return redirect('home')

def cotizacion(request):
    if request.method == 'POST':
        tipo_bodega_form = TipoBodegaForm(request.POST)
        bodega_form = BodegaForm()
        tipos_bodega = TipoBodega.objects.all()
        lista_bodegas = request.POST.get("lista_bodegas")
        monto_total = request.POST.get("monto_total")

        if len(lista_bodegas) > 0:
            bodegas_sel = Bodega.objects.filter(id__in=','.join(lista_bodegas))
        else:
            bodegas_sel = None

        if request.POST.get("tipo_bodega") is not None:
            bodega_form.fields['bodega'].queryset = Bodega.objects.filter(tipo_bodega=request.POST.get("tipo_bodega"))
        else:
            bodega_form.fields['bodega'].queryset = None
        
        return render(request, 'cotizacion.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form, "bodega_form":bodega_form, "lista_bodegas":lista_bodegas, "bodegas_sel":bodegas_sel, "monto_total":monto_total})
    else:
        tipo_bodega_form = TipoBodegaForm()
        tipos_bodega = TipoBodega.objects.all()
        monto_total = 0
        return render(request, 'cotizacion.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form, "monto_total":monto_total})

def agrega_bodega(request):
    if request.method == 'POST':
        tipo_bodega_form = TipoBodegaForm(request.POST)
        bodega_form = BodegaForm()
        tipos_bodega = TipoBodega.objects.all()
        lista_bodegas = request.POST.get("lista_bodegas")
        monto_total = int(request.POST.get("monto_total") or 0)

        if len(lista_bodegas) == 0:
            lista_bodegas = []
            lista_bodegas.append(request.POST.get("bodega"))
            print(lista_bodegas)
            bodegas_sel = Bodega.objects.filter(id__in=','.join(lista_bodegas))
            lista_bodegas = ','.join(lista_bodegas)
        else:
            print(lista_bodegas)
            lista_bodegas = lista_bodegas.split(',')
            lista_bodegas.append(request.POST.get("bodega"))
            bodegas_sel = Bodega.objects.filter(id__in=lista_bodegas)
            lista_bodegas = ','.join(lista_bodegas)

        monto_total = monto_total + TipoBodega.objects.filter(id=request.POST.get("tipo_bodega")).first().precio

        return render(request, 'cotizacion.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form, "bodega_form":bodega_form, "lista_bodegas":lista_bodegas, "bodegas_sel":bodegas_sel, "monto_total":monto_total})
    else:
        tipo_bodega_form = TipoBodegaForm()
        tipos_bodega = TipoBodega.objects.all()
        return render(request, 'cotizacion.html', {"tipos_bodega":tipos_bodega, "tipo_bodega_form":tipo_bodega_form})