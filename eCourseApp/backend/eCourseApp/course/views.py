from django.http import HttpResponse
from django.shortcuts import render

from course import views
# Create your views here.
def index(request):
    return HttpResponse("Huy dep trai sieu cap vo dich manh!")