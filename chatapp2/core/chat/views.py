from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
def chat(request, room_name):
    return render(request,'chat.html')