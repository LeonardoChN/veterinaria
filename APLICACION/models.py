from django.db import models

#DATOS DE FOREIGN_KEY
    
   #atencion 
class tipo_at (models.Model):
      atencion_at = models.CharField(max_length=45)
      def __str__(self):
           return self.atencion_at
      
      #mascotas
class tipo_m (models.Model):
      atencion_m = models.CharField(max_length=45)
      def __str__(self):
           return self.atencion_m
      
      #mascotas
class raza (models.Model):
      raza = models.CharField(max_length=45)
      def __str__(self):
           return self.raza

#DATOS PRINCIPALES FOREIGN_KEY

class funcionarios (models.Model):
    rut_f = models.CharField(max_length=45)
    nombre_fun = models.CharField(max_length=45)
    especialidad = models.CharField(max_length=45)
    user = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre_fun 
    
    

class mascota (models.Model):
  nombre_masc = models.CharField(max_length=45)
  tipo = models.ForeignKey(tipo_m,on_delete=models.CASCADE)
  raza = models.ForeignKey(raza,on_delete=models.CASCADE)
  def __str__(self):
      return self.nombre_masc 

class clientes (models.Model):
    rut_f = models.CharField(max_length=45)
    nombre_cli = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    fono = models.CharField(max_length=45)
    nom_mas = models.ForeignKey(mascota,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_cli

#esquema de la cita

class cita(models.Model):
    fecha = models.DateField()
    tipoat = models.ForeignKey(tipo_at,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(funcionarios,on_delete=models.CASCADE)
    cliente = models.ForeignKey(clientes,related_name = 'elclientexd',on_delete=models.CASCADE)
    mascota = models.ForeignKey(clientes,related_name = 'lamascotaxd',on_delete=models.CASCADE)
