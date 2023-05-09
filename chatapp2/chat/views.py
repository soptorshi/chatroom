from django.shortcuts import render, redirect

# Create your views here.

def lobby(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        username = request.POST.get('username')
        return redirect(f'/chat/{room_code}/?user={username}')
    return render(request, 'chat/lobby.html')
 

def chat(request, room_code):
    context = {
        'room_code':room_code, 'user':request.GET.get('user')
    }
    return render(request, 'chat/chat.html', context)