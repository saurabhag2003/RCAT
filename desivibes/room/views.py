from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from room.models import Room, Message,User
from django.http import HttpResponse, JsonResponse , Http404
from .models import Room,Message



@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})

@login_required
def room(request,room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(content=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request,room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages":list(messages.contents())})


# from django.core.serializers import serialize

# def getMessages(request, slug):
#     room_details = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room_details.id)
#     messages_data = [
#         {"user": m.user.username, "content": m.content}
#         for m in messages
#     ]
#     return JsonResponse({"messages": messages_data})


# from django.http import JsonResponse
# from .models import Room, Message

# def getMessages(request,room):
#     try:
#         room_details = Room.objects.get(slug=room)
#         messages = Message.objects.filter(room=room_details).order_by('timestamp')
        
#         messages_list = [
#             {
#                 "user": message.user.username,
#                 "value": message.content,
#                 "date": message.timestamp.strftime("%d %B %Y, %H:%M")
#             }
#             for message in messages
#         ]
        
#         return JsonResponse({"messages": messages_list})
    
#     except Room.DoesNotExist:
#         return JsonResponse({"error": "Room not found"}, status=404)
