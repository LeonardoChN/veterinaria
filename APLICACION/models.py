from django.db import models

#DATOS DE FOREIGN_KEY
    
   #atencion 
class tipo_at (models.Model):
    tipo_atencion= models.CharField(max_length=45)
    def __str__(self):
        return self.tipo_atencion
      
      #mascotas
class tipo_m (models.Model):
      tipo_mascota = models.CharField(max_length=45)
      def __str__(self):
           return self.tipo_mascota
      
      #mascotas
class raza (models.Model):
      raza = models.CharField(max_length=45)
      def __str__(self):
           return self.raza

#DATOS PRINCIPALES FOREIGN_KEY

class funcionarios (models.Model):
    rut_funcionario = models.CharField(max_length=45)
    nombre_funcionario = models.CharField(max_length=45)
    especialidad = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre_funcionario 
    
    

class mascota (models.Model):
  nombre_mascota = models.CharField(max_length=45)
  tipo = models.ForeignKey(tipo_m,on_delete=models.CASCADE)
  raza = models.ForeignKey(raza,on_delete=models.CASCADE)
  def __str__(self):
      return self.nombre_mascota 

class clientes (models.Model):
    rut_cliente = models.CharField(max_length=45)
    nombre_cliente = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    fono = models.CharField(max_length=45)
    nombre_mascota = models.ForeignKey(mascota,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_cliente

#esquema de la cita

class cita(models.Model):
    fecha = models.DateField()
    atencion = models.ForeignKey(tipo_at,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(funcionarios,on_delete=models.CASCADE)
    cliente = models.ForeignKey(clientes,related_name = 'elclientexd',on_delete=models.CASCADE)
    mascota = models.ForeignKey(mascota,on_delete=models.CASCADE)
