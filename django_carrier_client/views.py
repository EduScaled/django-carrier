from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from carrier_client.message import IncomingMessage
from .helpers import MessageManagerHelper, HttpResponseUnauthorized, is_auth

@csrf_exempt
def callback(request):
    if request.method == "POST":
        if not is_auth(request):
            return HttpResponseUnauthorized()
        for message_manager in MessageManagerHelper.get_message_managers_to_listen():
            message_manager.handle_message(
                IncomingMessage.create_from_bytes(request.body)
            )
        return HttpResponse()
    else: 
        raise Http404