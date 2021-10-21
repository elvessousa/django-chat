from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from room.models import Message, Room


def index(request):
    '''Login page'''

    return render(request, 'home.html')


def check(request):
    '''Checks for existing room'''

    room = request.POST['room']
    user = request.POST['user']

    if Room.objects.filter(name=room).exists():
        return redirect(f'/rooms/{room}/?user={user}')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()

        return redirect(f'/rooms/{room}/?user={user}')


def room(request, room):
    '''Room page'''

    user = request.GET.get('user')
    room_details = Room.objects.get(name=room)

    return render(request, 'room.html', {
        'room': room,
        'user': user,
        'details': room_details
    })


def send(request):
    '''Saves message to database'''

    user = request.POST['user']
    room = request.POST['room_id']
    message = request.POST['message']
    new_message = Message.objects.create(
        value=message,
        user=user,
        room=room
    )

    new_message.save()

    return HttpResponse('Message sent successfully.')


def messages(request, room):
    '''Gets messages from '''

    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({'messages': list(messages.values())})
