from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message


@csrf_exempt
def post_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(content=content)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def index(request):
    return render(request, 'chat_app/index.html')

def get_messages(request):
    messages = Message.objects.all().values('content', 'timestamp')
    return JsonResponse(list(messages), safe=False)

def post_message(request):
    content = request.POST.get('content')
    if content:
        Message.objects.create(content=content)
    return JsonResponse({'status': 'ok'})
