from django.shortcuts import render,HttpResponse
from .models import ToDoItems
# Create your views here.
#one page one f
def home(request):
    return render(request,"home.html")
def todos(request):
    items=ToDoItems.objects.all()# all data
    return render(request,"todos.html",{"todos":items})