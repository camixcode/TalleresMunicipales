from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')


def Form_Inscripcion_Taller(request):
    return render(request, 'core/Form_Inscripcion_Taller.html')

def Form_Instructor_Taller(request):
    return render(request, 'core/Form_Instructor_Taller.html')    

def Navbar(request):
    return render(request, 'core/Navbar.html')    