from django.db import models
import uuid

class Machine(models.Model):
    machine_id=models.UUIDField(default=uuid.uuid4,primary_key=True,)
    machine_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.machine_name
    
class Patient(models.Model):
    patient_id=models.UUIDField(default=uuid.uuid4,primary_key=True,)
    machine_name=models.ForeignKey(Machine, on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.patient_name
    
class Dose(models.Model):
    dose=models.FloatField()
    patient_name=models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "%s, %s " %(self.dose, self.patient_name)