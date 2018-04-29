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
    names = ['حمص','بابا غنوش']
    images = ['https://www.simplyrecipes.com/wp-content/uploads/2017/12/easy-hummus-horiz-a-1800.jpg','https://www.seriouseats.com/recipes/images/2014/02/20140225-baba-ganoush-recipe-food-lab-vegan-primary-3.jpg']
    descriptions = ['Hummus is a Levantine Arab dip or spread that is made from chickpeas (also known as garbanzo beans) that have been cooked and mashed, then blended with tahini (a paste made from sesame seeds), olive oil, lemon juice, garlic and salt.', 'Baba Ganouch is a thick sauce or spread made from pureed aubergines and sesame seeds, typical of eastern Mediterranean cuisine.']
    ingredients = [['chickpeas', 'olive oil', 'tahini', 'lemon juice', 'garlic', 'salt', 'pepper'], ['eggplant', 'garlic', 'lemon', 'tahini', 'basil', 'olive oil']]
    calories = ['166 calories per 100 gr'	,'400 cal per 100gr']
    story = ['Many regions around the world claim to be the place where hummus originated. The fact is, that because hummus has been around for so long, and in so many different variations, the exact origin has been lost in antiquity. Several cuisine-related sources speak of a folklore tale in which hummus is described as one of the oldest known prepared foods. Others speak of a legend that hummus was first prepared in the 12th century by Saladin, however this claim is highly disputed.','Baba Ghanoush is an eggplant dish that originated in Levant cuisine, frequently used for dipping. It is served mostly as an appetizer. The dish contains mainly olive oil and eggplant. Some cultures add in tahini, garlic, and pomegranate concentrate or lemon juice to add depth of flavor. In the Turkish culture, it is called both baba ghanoush and patlican salatasi,which means eggplant salad. Most of the time it is either boiled or broiled until it is soft and then mashed with additional flavors and olive oil.  Baba Ghanoush is eaten in many Middle Eastern countries such as Syria, Lebanon and extending as far as the territorial reach of the Ottoman empire. ']
    return render(request, 'views.html', {'title':titles[count].upper(), 'name':names[count],'image': images[count], 'description': descriptions[count], 'ingredients':ingredients[count], 'calorie' : calories[count], 'story': story[count]})