from django.urls import path
from.views import Admin_General, Admin_Taller, crear_Taller, home, Form_Inscripcion_Taller, Form_Instructor_Taller,Ins_Taller,Form_Evaluacion,crear_Material, Admin_Perfil, Admin_Muni, Admin_Postulacion, Admin_Pago, Admin_Cliente,Admin_Banner_Promocion,Admin_Instructor

urlpatterns = [
    path('', home, name="home"),
    path('Form_Inscripcion_Taller/', Form_Inscripcion_Taller, name="Form_Inscripcion_Taller"),
    path('Form_Instructor_Taller/', Form_Instructor_Taller, name="Form_Instructor_Taller"),
    path('PostularTaller/',Ins_Taller, name="Ins_Taller"),
    path('AdministradorTaller/',Admin_Taller, name="Admin_Taller"),
    path('Form_Evaluacion/',Form_Evaluacion, name="Form_Evaluacion"),
    path('AdministardorGeneral', Admin_General,name="Admin_General"),
    path('crearTaller', crear_Taller,name="crear_Taller"),
    path('CrearMaterial', crear_Material,name="crear_Material"),
    path('AdminPerfilesUsuarios', Admin_Perfil,name="Admin_Perfil"),
    path('AdminMunicipios', Admin_Muni,name="Admin_Muni"),
    path('AdminPago', Admin_Pago,name="Admin_Pago"),
    path('AdminPostulacion', Admin_Postulacion,name="Admin_Postulacion"),
    path('AdminClientes', Admin_Cliente,name="Admin_Cliente"),
    path('Admin_Instructor', Admin_Instructor,name="Admin_Instructor"),
    path('Admin_Banner', Admin_Banner_Promocion,name="Admin_Banner"),




]

