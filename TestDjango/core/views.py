from django.shortcuts import render
from .form import MaterialForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render

from core.models import Material

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def Form_Inscripcion_Taller(request):
    return render(request, 'core/Form_Inscripcion_Taller.html')


def Form_Instructor_Taller(request):
    return render(request, 'core/Form_Instructor_Taller.html')


def Ins_Taller(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Ins_Taller.html', datos)


def Admin_Taller(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Taller.html', datos)


def Form_Evaluacion(request):
    return render(request, 'core/Form_Evaluacion.html')


def Admin_General(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_General.html', datos)


def crear_Taller(request):
    return render(request, 'core/crear_Taller.html')


def crear_Material(request):
    datos = {
        'form': MaterialForm()
    }
    if request.method == 'POST':
        formmulario = MaterialForm(request.POST)
        if formmulario.is_valid:
            formmulario.save()
            messages.success(request,"Material registrado correctamente")
            datos['mensaje'] = "Guardados Correctamente"
            return redirect(to="Admin_General")

    return render(request, 'core/Crear_Material.html',datos)          


def Admin_Perfil(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Perfil.html', datos)


def Admin_Muni(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Muni.html', datos)


def Admin_Pago(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Pago.html', datos)


def Admin_Postulacion(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Postulacion.html', datos)


def Admin_Cliente(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Cliente.html', datos)


def Admin_Instructor(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Instructor.html', datos)


def Admin_Banner_Promocion(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Admin_Banner.html', datos)


def Tus_Talleres(request):
    material = Material.objects.all()
    datos = {
        'material': material
    }
    return render(request, 'core/Tus_Talleres.html', datos)



def Modificar_Material(request, id):
    material = Material.objects.get(idMaterial=id)
    datos = {
        'form': MaterialForm(instance=material)
    }
    if request.method == 'POST':
        formulario = MaterialForm(data=request.POST, instance=material)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            datos = {
                'form': MaterialForm(instance=material),
                'mensaje': "Modificado corretamente"
            }

    return render(request, 'core/Modificar_Material.html', datos)

    
def Eliminar_Material(request, id):
        material = Material.objects.get(idMaterial=id)
        material.delete()
        material = Material.objects.all()
        messages.success(request, "Usuario eliminado correctamente")
        datos = {
            'material': material
        }
        return render(request, 'core/Admin_General.html', datos)