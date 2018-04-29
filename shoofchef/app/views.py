from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# from models import UploadFile
import json
import requests
import os

# class UploadFileForm(forms.ModelForm):
# 	class Meta:
# 		model = UploadFile
# 		fields = '__all__'
#
# def upload(request):
# 	if request.method == 'POST':
# 		form = UploadFileForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			new_file = UploadFile(file=request.FILES['file'])
# 			new_file.save()
# 			new_file_name = str(new_file.file).split('/')[-1]
# 			return HttpResponse(json.dumps({'image':new_file_name}), content_type="application/json")
# 	else:
# 		form = UploadFileForm()
# 	images = [str(f.file).split('/')[-1] for f in UploadFile.objects.all()]
# 	return render(request, 'upload.html', {'form':form, 'images':images})


def home(request):	
	url = 'https://cloudvision-200712.appspot.com/images'
	files = {'imagefile': open('app/static/img/photo.png', 'rb')}
	r= requests.post(url, files=files)
	return render(request, 'home.html', {'data':r.content.decode("utf-8")})


def camera(request):	
	try:
		os.remove("app/static/img/photo.png")
	except:
		print("failed")
	return render(request, 'camera.html')


def views(request, count):
    count = int(count)
    titles = ['hummus','baba ganoush']
    images = ['https://www.simplyrecipes.com/wp-content/uploads/2017/12/easy-hummus-horiz-a-1800.jpg','https://www.seriouseats.com/recipes/images/2014/02/20140225-baba-ganoush-recipe-food-lab-vegan-primary-3.jpg']
    descriptions = ['A Levantine Arab dip made of chickpea paste with various additions, such as olive oil, fresh garlic, lemon juice, and tahini, often eaten with pitta bread, or as a meze. It is mostly eaten in the Levant.', 'Baba ghanoush is a Levantine dish of mashed cooked eggplant mixed with tahina (made from sesame seeds), olive oil, and various seasonings.']
    ingredients = [['chickpeas', 'olive oil', 'tahini', 'lemon juice', 'garlic', 'salt', 'pepper'], ['eggplant', 'garlic', 'lemon', 'tahini', 'basil', 'olive oil']]
    return render(request, 'views.html', {'title':titles[count].upper(), 'image':images[count], 'description':descriptions[count], 'ingredients':ingredients[count]})