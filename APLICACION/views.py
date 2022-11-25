from django.shortcuts import render

from APLICACION.forms import   formFunc,formMasc, formCliente,    formCita

from APLICACION.models import  funcionarios,mascota,clientes ,   cita

from django.shortcuts import redirect



##INDEX
def index(request):
    return render(request, 'APLICACION/index.html')


#---------  VISTAS  ---------

##FUNCIONARIOS
def listarfuncionario(request):
    fun = funcionarios.objects.all()
    data = {'funcionario': fun}
    return render(request, 'APLICACION/vistafun.html', data)
#
def agregarfun(request):
    form = formFunc()
    if request.method == 'POST' : 
        form = formFunc(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarfun.html', data)





## VISTA CITAS
def listarcitas(request):
    citas = cita.objects.all()
    data = {'cita': citas}
    return render(request, 'APLICACION/vistacitas.html', data)
#
def agregarcitas(request):
    form = formCita()
    if request.method == 'POST' : 
        form = formCita(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarcitas.html', data)





## VISTA PACIENTES
def listarcliente(request):
    cliente = clientes.objects.all()
    data = {'clientes': cliente}
    return render(request, 'APLICACION/vistaclient.html', data)
#
def agregarcliente(request):
    form = formCliente()
    if request.method == 'POST' : 
        form = formCliente(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarclient.html', data)


## VISTA MASCOTAS
def listarmascotas(request):
    masc = mascota.objects.all()
    data = {'mascota': masc}
    return render(request, 'APLICACION/vistaclient.html', data)
#
def agregarmascota(request):
    form = formMasc()
    if request.method == 'POST' : 
        form = formMasc(request.POST)
        if form.is_valid(): 
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarclient.html', data)






#--------------------------------------------
#---------  ELIMINAR Y ACTUALIZAR   ---------
#--------------------------------------------

'''
    #PACIENTES
def eliminarpaciente(request, id):
    paciente = PACIENTE.objects.get(id= id)
    paciente.delete()
    return redirect('/pacientes')

def actualzarpaciente (request, id) :
    paciente = PACIENTE.objects.get(id= id)
    form = formPaciente (instance=paciente)
    if request.method == 'POST':
        form = formPaciente(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarpaciente.html', data)



    #MEDICOS
def eliminarmedico(request, id):
    medico = MEDICOS.objects.get(id= id)
    medico.delete()
    return redirect('/medicos')

def actualizarmedico (request, id) :
    medico = MEDICOS.objects.get(id= id)
    form = formMedicos (instance=medico)
    if request.method == 'POST':
        form = formMedicos(request.POST, instance=medico)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarmedico.html', data)







        
    #CITAS
def eliminarcitas(request, id):
    cita = CITAS.objects.get(id= id)
    cita.delete()
    return redirect('/citas')

def actualizarcitas (request, id) :
    cita = CITAS.objects.get(id= id)
    form = formCitas (instance=cita)
    if request.method == 'POST':
        form = formCitas(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'APLICACION/agregarcitas.html', data)

'''