from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PdfSerializer
from rest_framework.response import Response
from rest_framework import status
from .forms import MyModelForm
from .models import Pdf
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from .Expert_resourse import Expert_Resource_Converter
from django.http import FileResponse
from django.conf import settings
from superadmin.models import Service
import os

import os
import pdb

# Create your views here.
@login_required
def get_index_page(request):
    services_ = Service.objects.all()
   
    if request.user.is_superuser:
        services_ = Service.objects.all()
        return render(request, 'superadmin/index.html',context={'service': services_})
    
    return render(request, 'user/index.html',context={'service': services_})

@api_view(['GET'])
def index(request):
    file=Pdf.objects.get(id=5)
    return render(request, 'user/index.html', context={"file":file})


def upload_file(request):
    return render(request, 'user/upload_file.html')
    


@api_view(['POST'])
def perform_services(request):  
   
    data=request.data
    print("data",data)
    serializer=PdfSerializer(data=request.data)
   # /Users/manzoorhussain/Documents/ILOVEPDF/pdf/media/pdf_input/Nicholas_Eager.docx
   # data=Expert_Resource_Converter("/Users/manzoorhussain/Documents/ILOVEPDF/pdf_input/Palak_Singh_Formatted_CV.docx")
    if serializer.is_valid():
        serializer.save()
    
        obj=Pdf.objects.all().last()
        path=str(obj.pdf)
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        return Response(status=200)
    return Response(status=400,data=serializer.errors)
    
    # path="/Users/manzoorhussain/Documents/ILOVEPDF/pdf/media/"+path
    # try:
    #     Expert_Resource_Converter(path)
    # except Exception as e:
    #     print(e)
   # return render(request, 'user/index.html')
  
  

api_view(['GET'])
def download_docx(request):
    print("dowload")
    
    obj = Pdf.objects.all().last()
    if obj:
        
        id = obj.id
        file_name = str(obj.pdf)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        filename = os.path.basename(file_path)
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        # Open the file and write its contents to the response
        with open(file_path, 'rb') as file:
            response.write(file.read())
        
            os.remove(file_path)
            obj=Pdf.objects.get(id=id)
            obj.delete()
        
        
        
            return response
        raise Http404
    response=400
    return response













   
