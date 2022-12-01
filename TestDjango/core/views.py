from django.shortcuts import render
from .form import MaterialForm
from django.contrib.auth import authenticate, login

from core.models import Material

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def Form_Inscripcion_Taller(request):
    return render(request, 'core/Form_Inscripcion_Taller.html')

def Form_Instructor_Taller(request):
    return render(request, 'core/Form_Instructor_Taller.html')    
 
def Ins_Taller(request):
    material =Material.objects.all()
    datos = {
        'material':material
    }
    return render (request, 'core/Ins_Taller.html', datos)

def Admin_Taller (request):
    material =Material.objects.all()
    datos = {
        'material':material
    }
    return render (request, 'core/Admin_Taller.html', datos)    

def Form_Evaluacion (request):
    return render (request, 'core/Form_Evaluacion.html')    

def Admin_General (request):
    material =Material.objects.all()
    datos = {
        'material':material
    }
    return render (request, 'core/Admin_General.html',datos)  

def crear_Taller (request):
    return render (request, 'core/crear_Taller.html')    

def crear_Material (request):
    datos = {
        'form' : MaterialForm()
    }
    if request.method == 'POST':
        formulario = MaterialForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos Guardados Correctamente"       
    return render (request, 'core/crear_Material.html', datos)    

def Admin_Perfil (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Perfil.html',datos)  

def Admin_Muni (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Muni.html',datos)          

def Admin_Pago (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Pago.html',datos)         

def Admin_Postulacion (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Postulacion.html',datos)          

def Admin_Cliente (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Cliente.html',datos)

def Admin_Instructor (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Instructor.html',datos) 

def Admin_Banner_Promocion (request):
        material =Material.objects.all()
        datos = {
            'material':material
        }
        return render (request, 'core/Admin_Banner.html',datos)               