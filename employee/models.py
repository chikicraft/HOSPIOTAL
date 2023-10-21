from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    paciente = models.CharField(max_length=100)  
    fecha_hora = models.DateTimeField()  
    medico = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.paciente) 
    class Meta:  
        db_table = "employee"  