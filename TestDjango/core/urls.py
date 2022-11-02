from django.urls import path
from.views import Admin_Taller, home, Form_Inscripcion_Taller, Form_Instructor_Taller,Ins_Taller,Form_Evaluacion

urlpatterns = [
    path('', home, name="home"),
    path('Form_Inscripcion_Taller/', Form_Inscripcion_Taller, name="Form_Inscripcion_Taller"),
    path('Form_Instructor_Taller/', Form_Instructor_Taller, name="Form_Instructor_Taller"),
    path('PostularTaller/',Ins_Taller, name="Ins_Taller"),
    path('AdministradorTaller/',Admin_Taller, name="Admin_Taller"),
    path('Form_Evaluacion/',Form_Evaluacion, name="Form_Evaluacion"),
    
]