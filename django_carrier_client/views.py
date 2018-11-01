from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from carrier_client.message import IncomingMessage
from .helpers import MessageManagerHelper

@csrf_exempt
def callback(request):
    if request.method == "POST":
        for message_manager in MessageManagerHelper.get_message_managers_to_listen():
            message_manager.handle_message(
                IncomingMessage.create_from_bytes(request.body)
            )
        # TODO must return meaningful response
        return HttpResponse()
    else: 
        raise Http404