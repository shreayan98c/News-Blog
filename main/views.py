import json
import requests
from .models import Article
from .forms import NewUserForm
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def homepage(request):

	url = ('https://newsapi.org/v2/top-headlines?'
       	   'country=us&'
       	   'apiKey=d4ee2618b49c47ddab513ef84d6dd400')
	response = requests.get(url)
	json_data = json.loads(response.text)
	articles = json_data['articles']

	for i, article in enumerate(articles):
		source = article['source']['name']
		author = article['author']
		title = article['title']
		description = article['description']
		url = article['url']
		urlToImage = article['urlToImage']
		publishedAt = article['publishedAt']
		content = article['content']
		
		article = Article(source=source, 
 						  author=author, 
						  title=title, 
						  description=description, 
						  url=url, 
						  urlToImg=urlToImage, 
						  publishedAt=publishedAt, 
						  content=content)

		article.save()

	return render(request=request,
				  template_name='main/home.html',
				  context={"articles":Article.objects.all})

def register(request):
	if request.method=="POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f"New account created: {username}")
			login(request, user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

			return render(request=request,
						  template_name="main/register.html",
						  context={"form":form})

	form = NewUserForm
	return render(request=request,
				  template_name='main/register.html',
				  context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")

	form = AuthenticationForm()
	return render(request=request,
				  template_name="main/login.html",
				  context={"form":form})

def single_slug(request, single_slug):
	articles = [a for a in Article.objects.all()]
	article_titles = [a.title for a in Article.objects.all()]
	if single_slug in article_titles:
		return render(request=request,
					  template_name="main/article.html",
					  context={"single_slug":articles})

	return HttpResponse(f"{single_slug} does not correspond to anything.")