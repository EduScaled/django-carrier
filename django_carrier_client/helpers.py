from django.http import HttpResponse
from .models import AuthToken

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

class MessageManagerHelperSingleton:
    instance = None

    class __MessageManagerHelperSingleton:
        def __init__(self):
            self._to_listen = []

    def __init__(self):
        if not MessageManagerHelperSingleton.instance:
            MessageManagerHelperSingleton.instance = MessageManagerHelperSingleton.__MessageManagerHelperSingleton()

    def set_manager_to_listen(self, manager):
        self.instance._to_listen.append(manager)   
        
    def get_message_managers_to_listen(self):
        return self.instance._to_listen 

AUTH_HEADER = "HTTP_AUTHORIZATION"

MessageManagerHelper = MessageManagerHelperSingleton()

def is_auth(request):
    return AUTH_HEADER in request.META and request.META[AUTH_HEADER] in get_auth_tokens()

def get_auth_tokens():
    return list(AuthToken.objects.filter(is_active=True).values_list('token', flat=True).distinct())