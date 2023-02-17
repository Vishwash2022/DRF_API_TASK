from django.shortcuts import render
from .models import  Machine, Patient, Dose
from rest_framework.views import APIView
from .serializers import DoseSerializer
from rest_framework.response import Response



def show(request):
    patient=Patient.objects.all()
    dose=Dose.objects.all()
    return render(request, 'show.html', {'patient':patient, 'dose':dose})




class ShowAPI(APIView):
    def get(self, request,pk):
        try:
            machine_name=Machine.objects.filter(machine_id=pk)
            
            patient_name=Patient.objects.filter(machine_name_id=pk).all()
            p=len(patient_name)
            query=patient_name[p-1:]
            name=list(query)[0]
            querys=Patient.objects.get(patient_name=name)
            
            queryset=Dose.objects.filter(patient_name=querys).all()
            l=len(queryset)
            queryset=queryset[l-1:]
            
            serializer=DoseSerializer(queryset, many=True)
            
            return Response({
                'status':True,
                'message':'patient fetched',
                'data':serializer.data
            })
        except Exception as e:
            return Response({
                'status':False,
                'message':'Not Fetched',
                'data':{}
            })