from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from models import UploadFile
import json
import requests
import os

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = UploadFile
		fields = '__all__'

def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			new_file = UploadFile(file=request.FILES['file'])
			new_file.save()
			new_file_name = str(new_file.file).split('/')[-1]
			return HttpResponse(json.dumps({'image':new_file_name}), content_type="application/json")
	else:
		form = UploadFileForm()
	images = [str(f.file).split('/')[-1] for f in UploadFile.objects.all()]
	return render(request, 'upload.html', {'form':form, 'images':images})	

def home(request):	
	url = 'https://cloudvision-200712.appspot.com/images'
	files = {'imagefile': open('app/static/menu.jpg', 'rb')}
	r= requests.post(url, files=files)
	return render(request, 'home.html', {'data':r.content})

def camera(request):	
	try:
		os.remove("app/static/img/photo.png")
	except:
		print("failed")
	return render(request, 'camera.html')	