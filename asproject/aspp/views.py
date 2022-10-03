from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello App!</h1>")
	return render(request, "home.html", {})

def about(request, *args, **kwargs):
	my_context = {
		"my_key": "This is arbitrary",
		"my_number": 123
	}
	return render(request, "about.html", my_context)

def all_articles(request, *args, **kwargs):
	article_list = Article.objects.all()
	return render(request, "articles/article.html", {
		'article_list':article_list
	})

def read(request, article_id, *args, **kwargs):
	article = Article.objects.get(pk=article_id)
	file = article.content
	file_content = file.read()
	file.close()
	return render(request, 'articles/read.html', {
		'article': article,
		'content':file_content
	})

def blog(request, *args, **kwargs):
	return render(request, "blog.html", {})

def contact(request, *args, **kwargs):
	return render(request, "contact.html", {})

def donate(request, *args, **kwargs):
	return render(request, "donate.html", {})

def search(request, *args, **kwargs):
	article_list = Article.objects.all()

	if (request.method == "POST"):
		searched = request.POST.get('searched', '')
		articles = Article.objects.filter(tags__contains=searched)
		return render(request, "search.html", {
			'searched': searched,
			'articles': articles
		})
	else:
		return render(request, "search.html", {})
