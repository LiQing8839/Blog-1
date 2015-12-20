#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,Http404
from models import *

from django.template.context import RequestContext
import json	
# Create your views here.


def hello(request):
	return HttpResponse('HI,you get me !')


def main(request):
	return render_to_response("base.html")


def board(request):
	return render_to_response("test.html")

def article(request):
    blogs = Article.objects.all()  #获取全部的Article对象
    return render(request, 'article.html', {'blogs' : blogs}) 