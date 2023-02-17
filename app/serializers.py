from rest_framework import serializers
from .models import Machine, Patient, Dose




class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Machine
        fields="__all__"
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        models=Patient
        fields="__all__"
        
class DoseSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        content={
            'machine_id':instance.patient_name.machine_name.machine_id,
            'patient_id':instance.patient_name.patient_id,
            'patient_name':instance.patient_name.patient_name,
            'dose_id':instance.id,
            'dose':instance.dose,
        }
        return content
    
    class Meta:
        model=Dose
        fields="__all__"