from django.urls import path
from.views import home, Form_Inscripcion_Taller, Form_Instructor_Taller, Navbar

urlpatterns = [
    path('home', home, name="home"),
    path('Form_Inscripcion_Taller/', Form_Inscripcion_Taller, name="Formulario_Inscripcion_Taller"),
    path('Form_Instructor_Taller/', Form_Instructor_Taller, name="Formulario_Instructor_Taller"),
    path('Navbar/', Navbar, name="Navbar"),
]