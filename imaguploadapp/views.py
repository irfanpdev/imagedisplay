from django.shortcuts import render,HttpResponse
from .models import *
import pathlib
from django.contrib import messages

# Create your views here.



def index(request):
    return render(request,"show.html")

def imgupld(request):
    if request.method=='POST':
        img=request.FILES['imgurl']
        imgType=request.POST['imgtype']
        file_extension = pathlib.Path(str(img)).suffix
        FileExtensionlist=['.png','.jpg','.jpeg']
        if file_extension in FileExtensionlist:
            newimg=ImageUploads.objects.create(imgname=img,imgtype=imgType)
        #return HttpResponse('The file has been uploaded successfully',newimg.imgname)
            messages.success(request,'Your file has been uploaded successfully')
            return render(request,"show.html")

        else:
            messages.info(request,'Your have selected invalid file type')
            return render(request,"show.html")